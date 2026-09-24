# Hipótesis automáticas — 2026-09-24 17:13 UTC
_Generado por shadow_postmortem.py sobre 592028 resoluciones (PNL=+66418.81€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=482)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.235 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.257 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.139)

- **PATRÓN** `banda_z` > `4.083` → IC=+0.164 (n=546)

  - _Acción_: Kelly boost +0.82€ cuando `banda_z` > 4.083 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=585)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `3000.2192` → IC=+0.150 (n=364)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3000.2192 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.128 (n=170)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 95.0 (IC base=+0.047)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=419)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=351)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.258 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.148)

- **PATRÓN** `banda_z` > `4.303` → IC=+0.176 (n=436)

  - _Acción_: Kelly boost +0.88€ cuando `banda_z` > 4.303 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=496)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `4494.3377` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4494.3377 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 96.0 (IC base=+0.048)

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
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=88)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=101)

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

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

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
- **FILTRO** `restante_s_al_confirmar` < `146.02` → IC=-0.233 (n=7033)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.02
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=21113)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.26` → IC=-0.249 (n=921)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.26
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2766)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `497.8` → IC=-0.148 (n=362)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 497.8
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1089)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `126.4` → IC=-0.308 (n=866)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.4
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2600)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.09` → IC=-0.224 (n=1689)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.09
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=5068)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `126.11` → IC=-0.357 (n=1386)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.11
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=4158)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.229 (n=356)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=408)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.197 (n=176)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=534)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=560)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.204 (n=13805)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=3474)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5621.0485` → IC=+0.178 (n=2213)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5621.0485 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=11256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=13787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.230 (n=10820)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5639)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7798.6476` → IC=+0.174 (n=2127)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7798.6476 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=1634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `16019.7856` → IC=+0.242 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16019.7856 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `15869.986` → IC=+0.216 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15869.986 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.168 (n=323)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.615 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.147 (n=236)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4624.034 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.139 (n=519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.105)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=819)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.105)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=2395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.337 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.357 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `3730.6434` → IC=+0.233 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3730.6434 (IC base=+0.231)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.141 (n=660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.240 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=538)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1311.0387` → IC=+0.151 (n=654)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1311.0387 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.433 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.165 (n=1080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 7.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=582)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.316 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=724)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.160)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.364 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=188)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `1256.1353` → IC=+0.155 (n=227)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1256.1353 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.195 (n=382)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.355 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=11423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=10969)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.226 (n=3784)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.174 (n=2639)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.182 (n=1937)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.71 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.248 (n=838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.352 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.247)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=2581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2240)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.321 (n=856)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2553)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.196 (n=1955)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.430 (n=467)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `2073.3909` → IC=+0.438 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2073.3909 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.437 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `19031.9918` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 19031.9918 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.449 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.447 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3366.033 (IC base=+0.435)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.200 (n=33959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.235 (n=15177)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.176 (n=5869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6334)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=6089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=2157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=6183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=6168)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=3041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.265 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=5622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.254 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=5680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=5679)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5158)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.127 (n=4771)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.15 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.139 (n=5160)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=6306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.84` → IC=+0.140 (n=4765)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.84 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2600)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.11` → IC=+0.132 (n=2375)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.11 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.139 (n=2562)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=3512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.4` → IC=+0.143 (n=2364)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.4 (IC base=+0.123)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=2558)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=2404)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=2605)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.3` → IC=+0.137 (n=2405)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.3 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `4097.0073` → IC=+0.312 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4097.0073 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.339 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `4255.42` → IC=+0.302 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4255.42 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.334 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.382 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1466.3152` → IC=+0.310 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.3152 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.353 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.345)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.367 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.345)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.382 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.345)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.352 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.345)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.380 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.345)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.442 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.440 (n=431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `2546.95` → IC=+0.435 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2546.95 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.450 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `1988.111` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.111 (IC base=+0.440)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.316 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.289 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.258)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.316 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.289 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.258)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4856` → IC=+0.122 (n=8014)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.4856 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.9829` → IC=+0.244 (n=2672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9829 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.8436` → IC=+0.249 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8436 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.634` → IC=+0.249 (n=2260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.634 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.354` → IC=+0.186 (n=2125)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 8.354 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.247 (n=2161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2117 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `1.0481` → IC=+0.259 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0481 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.3047` → IC=+0.219 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3047 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.4638` → IC=+0.202 (n=5482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4638 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.134 (n=9667)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.57 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.6159` → IC=+0.195 (n=705)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6159 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.1534` → IC=+0.174 (n=3068)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1534 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6987` → IC=+0.181 (n=1487)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6987 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.0558` → IC=+0.175 (n=1532)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0558 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.1677` → IC=+0.223 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1677 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.5708` → IC=+0.201 (n=5077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5708 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.211 (n=5469)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=+0.065)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.180 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.175 (n=608)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.165 (n=1812)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.168 (n=1220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.136` → IC=+0.270 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.136 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.207 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.163 (n=1694)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.249 (n=1222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.279 (n=455)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=1235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0531` → IC=+0.294 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0531 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.421` → IC=+0.235 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.421 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.428` → IC=+0.247 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.428 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.231 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.260 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6222` → IC=+0.241 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6222 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.230 (n=923)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.252 (n=461)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=1448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9878` → IC=+0.268 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9878 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.2018` → IC=+0.222 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2018 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.5823` → IC=+0.221 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5823 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.827` → IC=+0.256 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.827 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.220 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.228 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.242 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7478` → IC=+0.218 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7478 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.229 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16041.9297` → IC=+0.225 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16041.9297 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.178 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0767` → IC=+0.163 (n=479)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0767 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6932` → IC=+0.172 (n=1437)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6932 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.156 (n=1284)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.254` → IC=+0.160 (n=230)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.254 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.261` → IC=+0.141 (n=1308)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.261 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.150 (n=1437)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2049 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1567` → IC=+0.177 (n=382)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1567 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4183` → IC=+0.152 (n=1327)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4183 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4164` → IC=+0.147 (n=1326)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4164 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `410.0` → IC=+0.149 (n=1243)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 410.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.210 (n=592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=1867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.224` → IC=+0.250 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.224 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.2115` → IC=+0.189 (n=1773)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2115 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3609` → IC=+0.199 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3609 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.8344` → IC=+0.205 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8344 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=1281)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.220 (n=1528)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6005` → IC=+0.215 (n=1526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6005 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.249 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.637` → IC=+0.242 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.637 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3558` → IC=+0.266 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3558 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7743` → IC=+0.205 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7743 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.2085` → IC=+0.220 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2085 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1887.161` → IC=+0.225 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.161 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.215 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.153 (n=99)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2208)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.217 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.3692` → IC=+0.321 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3692 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.7929` → IC=+0.330 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7929 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.739` → IC=+0.158 (n=711)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.739 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.323 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `1.2014` → IC=+0.338 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2014 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4057` → IC=+0.341 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4057 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.335 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.329 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.68 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.163 (n=553)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8504 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.5204` → IC=+0.176 (n=693)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5204 (IC base=+0.017)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.177 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=318)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.208 (n=94)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=284)

- **FILTRO** `ibs_20min` > `0.2564` → IC=-0.126 (n=2176)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2564
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=1073)

- **FILTRO** `sigma_ewma_delta_pct` > `8.673` → IC=-0.209 (n=348)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.673
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2901)

- **PATRÓN** `ibs_20min` > `0.7846` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7846 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.5947` → IC=+0.271 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5947 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.6541` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6541 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `0.7836` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7836 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.2264` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2264 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.2564` → IC=+0.128 (n=1073)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.2564 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.6927` → IC=+0.258 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6927 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.7131` → IC=+0.242 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7131 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` > `0.9027` → IC=+0.221 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9027 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.238 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1501` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1501 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.268 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6622` → IC=-0.185 (n=563)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6622
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1691)

- **FILTRO** `ibs_20min` < `0.7114` → IC=-0.155 (n=1487)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7114
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=767)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.201 (n=413)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1841)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.203 (n=825)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=2489)

- **PATRÓN** `dist_vwap_pct` > `0.7895` → IC=+0.324 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7895 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2685` → IC=+0.315 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2685 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9845` → IC=+0.290 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9845 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.304 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.297 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.3923` → IC=+0.311 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3923 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.294 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8811` → IC=+0.263 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8811 (IC base=-0.024)

- **PATRÓN** `volumen_regimen` < `0.7389` → IC=+0.251 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7389 (IC base=-0.024)

- **PATRÓN** `volumen_regimen` > `1.092` → IC=+0.280 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.092 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1027` → IC=+0.273 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1027 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.1538` → IC=+0.257 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1538 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.434` → IC=+0.246 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.434 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.196 (n=3356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0098 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4755` → IC=+0.189 (n=8977)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4755 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.7692` → IC=+0.289 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7692 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.605` → IC=+0.156 (n=4737)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.605 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.247 (n=3192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.266 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4663` → IC=+0.240 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4663 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6685` → IC=+0.240 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6685 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.267 (n=5316)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.153 (n=3342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0091 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5478` → IC=+0.154 (n=8813)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5478 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7244` → IC=+0.234 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7244 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2492` → IC=+0.239 (n=2799)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2492 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7106` → IC=+0.239 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7106 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.2069` → IC=+0.246 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2069 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2441` → IC=+0.301 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2441 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.256 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.3191` → IC=+0.255 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3191 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.262 (n=3767)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 84.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.525` → IC=-0.158 (n=530)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.525
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1777)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.267 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.799` → IC=+0.211 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.799 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.271 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.433` → IC=+0.177 (n=292)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.433 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.1547` → IC=+0.197 (n=397)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.1547 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.174 (n=379)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 14.0 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1599` → IC=+0.443 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1599 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.3948` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3948 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.464 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8588` → IC=+0.158 (n=671)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8588 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.174 (n=511)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6736` → IC=+0.166 (n=825)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6736 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.223 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.200 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `245.0` → IC=+0.193 (n=392)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 245.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1614` → IC=+0.218 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1614 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `0.613` → IC=+0.213 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.613 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2715` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2715 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.218 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.236 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `471.0` → IC=+0.210 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 471.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.287 (n=529)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=1590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=1420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.736` → IC=+0.280 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.736 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.1042` → IC=+0.258 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1042 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `3.4277` → IC=+0.261 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4277 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.253 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1959.2048` → IC=+0.253 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1959.2048 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.314 (n=574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.6083` → IC=+0.282 (n=1266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6083 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.329 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.289 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2222 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.812` → IC=+0.296 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.812 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.307 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `1.594` → IC=+0.283 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.594 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.286 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `1875.8832` → IC=+0.299 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.8832 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.285 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.281)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2855` → IC=-0.184 (n=491)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2855
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=1473)

- **FILTRO** `ibs_20min` > `0.7745` → IC=-0.186 (n=593)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7745
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1783)

- **PATRÓN** `ibs_20min` > `0.9105` → IC=+0.177 (n=491)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9105 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.227 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.2169` → IC=+0.209 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2169 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `0.9898` → IC=+0.234 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9898 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.5867` → IC=+0.210 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5867 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.255 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.5105` → IC=+0.262 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5105 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.243 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` > `0.1552` → IC=+0.207 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1552 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` < `0.6852` → IC=+0.201 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6852 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1643` → IC=+0.211 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1643 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8269` → IC=+0.261 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8269 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1743` → IC=+0.236 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1743 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.248 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.72` → IC=-0.199 (n=1065)

  - _Acción_: SKIP cuando `ibs_20min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.280 (n=1067)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.231 (n=549)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=1668)

- **FILTRO** `sigma_ewma_delta_pct` > `4.705` → IC=-0.180 (n=485)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.705
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=1732)

- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.280 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.72 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.8477` → IC=+0.333 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8477 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.607` → IC=+0.163 (n=336)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.607 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8758` → IC=+0.302 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8758 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `0.7299` → IC=+0.292 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7299 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.292 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.297 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.324 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.312 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.213 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.218 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.247 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.208 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.205 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.4844` → IC=+0.220 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4844 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `1.5706` → IC=+0.199 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5706 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.237 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.316 (n=869)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.293 (n=611)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` > `0.9118` → IC=+0.344 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9118 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.316 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.299 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.301 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.321 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.292 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2630.254` → IC=+0.291 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2630.254 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.297 (n=939)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.280 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.273 (n=698)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.3945` → IC=+0.304 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3945 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.3038` → IC=+0.280 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3038 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.9769` → IC=+0.272 (n=1591)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9769 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.494` → IC=+0.288 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.494 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.274 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.305 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.340 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `1.4305` → IC=+0.272 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4305 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.1512` → IC=+0.275 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1512 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2622.2916` → IC=+0.274 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2622.2916 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.170 (n=2620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.202 (n=2613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0903` → IC=+0.187 (n=2611)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0903 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=8161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.5775` → IC=+0.217 (n=7832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5775 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1763` → IC=+0.197 (n=3409)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1763 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.353` → IC=+0.254 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.353 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2135` → IC=+0.160 (n=5181)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2135 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.161 (n=5183)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6297 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.195 (n=1174)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5598` → IC=+0.170 (n=3304)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5598 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6235` → IC=+0.177 (n=2503)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6235 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2401.4762` → IC=+0.169 (n=5221)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2401.4762 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.180 (n=6754)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 116.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.182 (n=4992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0812` → IC=+0.207 (n=2495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0812 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.4783` → IC=+0.226 (n=7480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4783 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.233` → IC=+0.158 (n=5451)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.233 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.348` → IC=+0.196 (n=1271)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.348 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.151 (n=5421)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1756 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.222 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.166 (n=2992)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.2559` → IC=+0.170 (n=3081)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2559 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.172 (n=6442)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 116.0 (IC base=+0.167)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.219 (n=446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.190 (n=447)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0083 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3452` → IC=+0.206 (n=1337)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3452 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=1407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=894)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.8961` → IC=+0.276 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8961 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.312 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.233 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.179 (n=1236)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.250 (n=867)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1882` → IC=+0.290 (n=647)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1882 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.264 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.25` → IC=+0.251 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.25 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.234 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.254 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4215` → IC=+0.263 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4215 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1804.9372` → IC=+0.244 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1804.9372 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.228 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.201 (n=389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=1230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.4068` → IC=+0.227 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4068 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2117` → IC=+0.214 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2117 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.235 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.164 (n=1165)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2653 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.0753` → IC=+0.170 (n=529)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0753 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.205 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5005` → IC=+0.182 (n=498)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5005 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `15957.2347` → IC=+0.165 (n=529)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 15957.2347 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.157 (n=1274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0057 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.293` → IC=+0.158 (n=1271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.293 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5649` → IC=+0.186 (n=1271)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.5649 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1339` → IC=+0.160 (n=1262)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1339 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.883` → IC=+0.199 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.883 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.155 (n=1271)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2145 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.155 (n=389)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.145 (n=1159)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4202` → IC=+0.135 (n=1159)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4202 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.169 (n=360)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 215.0 (IC base=+0.136)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.218 (n=597)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.2296` → IC=+0.214 (n=877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2296 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.868` → IC=+0.275 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.868 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1322` → IC=+0.198 (n=512)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1322 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.6328` → IC=+0.199 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6328 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.8468` → IC=+0.212 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8468 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `1960.0448` → IC=+0.201 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1960.0448 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.229 (n=1089)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.248 (n=363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.276 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.2407` → IC=+0.255 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2407 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.266 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3558` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3558 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7801` → IC=+0.213 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7801 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `3.4055` → IC=+0.234 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4055 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1887.4151` → IC=+0.218 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.4151 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.211 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.217)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.171 (n=1102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0066 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4364` → IC=+0.158 (n=1252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4364 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.3792` → IC=+0.197 (n=1251)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3792 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1614` → IC=+0.180 (n=829)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1614 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.003` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.003 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0418` → IC=+0.144 (n=1101)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0418 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6274` → IC=+0.149 (n=1251)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6274 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2461` → IC=+0.196 (n=264)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2461 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.5375` → IC=+0.149 (n=539)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5375 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.5288` → IC=+0.169 (n=409)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5288 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `6488.9388` → IC=+0.184 (n=834)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 6488.9388 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.146 (n=1189)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 164.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.153 (n=1322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.3842` → IC=+0.142 (n=1321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3842 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6374` → IC=+0.171 (n=1321)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6374 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.5895` → IC=+0.132 (n=1537)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5895 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.964` → IC=+0.170 (n=464)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 6.964 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8485` → IC=+0.147 (n=881)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8485 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.194 (n=191)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.135 (n=800)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `10007.3401` → IC=+0.159 (n=599)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10007.3401 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=641)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5172` → IC=+0.204 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5172 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0956` → IC=+0.226 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0956 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.733` → IC=+0.252 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.733 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.131 (n=1416)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2233 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6454` → IC=+0.123 (n=1413)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6454 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.0711` → IC=+0.123 (n=593)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0711 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5459` → IC=+0.141 (n=600)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5459 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1479)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2892.276` → IC=+0.200 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2892.276 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.137 (n=1088)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.152 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0061 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.156 (n=478)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.210 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.0029` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 1.0029 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.138 (n=1328)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2001 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.006` → IC=+0.141 (n=232)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.006 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6359` → IC=+0.135 (n=478)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6359 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.167 (n=175)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4542` → IC=+0.133 (n=429)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4542 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.133 (n=428)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `1463.3817` → IC=+0.135 (n=1281)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1463.3817 (IC base=+0.113)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.213 (n=901)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.205 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.7396` → IC=+0.260 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7396 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.5093` → IC=+0.224 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5093 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.576` → IC=+0.242 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.576 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.205 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2075 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6239` → IC=+0.213 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6239 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.268 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1492` → IC=+0.212 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1492 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4095` → IC=+0.208 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4095 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2820.7088` → IC=+0.211 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2820.7088 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.227 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0172` → IC=+0.205 (n=931)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0172 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.220 (n=466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.220 (n=681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.4375` → IC=+0.245 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4375 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.2417` → IC=+0.221 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2417 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.9142` → IC=+0.203 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9142 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.442` → IC=+0.243 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.442 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6302` → IC=+0.215 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6302 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.293 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.2134` → IC=+0.193 (n=1103)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2134 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.199 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2592.2873` → IC=+0.207 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2592.2873 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.159 (n=623)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0039 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.180 (n=623)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0089 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1004` → IC=+0.153 (n=624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1004 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=932)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.5469` → IC=+0.188 (n=1667)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5469 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.3941` → IC=+0.181 (n=559)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3941 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.719` → IC=+0.175 (n=853)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.719 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8754` → IC=+0.164 (n=1095)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8754 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `1.21` → IC=+0.156 (n=547)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.21 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.174 (n=519)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.165 (n=600)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5403` → IC=+0.154 (n=600)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5403 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=2120)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `12428.4336` → IC=+0.162 (n=622)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 12428.4336 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.167 (n=1647)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 162.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.137 (n=1308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0057 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=1976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.6579` → IC=+0.137 (n=1954)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6579 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2134` → IC=+0.122 (n=1741)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2134 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.2258` → IC=+0.125 (n=1655)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.2258 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2736.3413` → IC=+0.122 (n=1746)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2736.3413 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.123 (n=605)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 20.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.123 (n=470)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.152 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 9.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.67` → IC=+0.179 (n=313)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.67 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.154 (n=157)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6182 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `15008.644` → IC=+0.144 (n=313)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 15008.644 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.147 (n=148)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 147.0 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.212 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.155 (n=624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6012` → IC=+0.182 (n=549)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6012 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4881` → IC=+0.151 (n=718)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4881 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.153 (n=243)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2142` → IC=+0.141 (n=624)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2142 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.167 (n=283)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0609 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.202 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1013` → IC=+0.155 (n=540)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1013 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.149 (n=614)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `382.0` → IC=+0.148 (n=592)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 382.0 (IC base=+0.136)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.255 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.197 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.007 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.0958` → IC=+0.208 (n=193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0958 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.9737` → IC=+0.269 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9737 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.154` → IC=+0.212 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.154 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.883` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.883 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.199 (n=386)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8363 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2624` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2624 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.3993` → IC=+0.225 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3993 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.4105` → IC=+0.231 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4105 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `12421.138` → IC=+0.223 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12421.138 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.0812` → IC=+0.161 (n=181)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0812 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `0.6864` → IC=+0.122 (n=239)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.6864 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.128 (n=127)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `3825.7125` → IC=+0.120 (n=485)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 3825.7125 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3436` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3436
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=489)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.181 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.009 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.5317` → IC=+0.136 (n=415)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.5317 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.7317` → IC=+0.205 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7317 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.6565` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6565 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.234` → IC=+0.205 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.234 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.0697` → IC=+0.148 (n=365)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0697 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.1842` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1842 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.2136` → IC=+0.170 (n=180)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2136 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=452)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3078.7088` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3078.7088 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.151 (n=393)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7082` → IC=+0.136 (n=174)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.7082 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5916` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5916 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `2537.9804` → IC=+0.121 (n=262)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2537.9804 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.120 (n=343)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 44.0 (IC base=+0.073)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0068 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6778` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6778 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.155 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0091 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.178` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.178 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8853` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8853 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.136 (n=201)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6515 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.6848` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.6848 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.206 (n=3339)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=10446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.216 (n=10015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9744` → IC=+0.205 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9744 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.634` → IC=+0.226 (n=4836)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.634 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8815` → IC=+0.165 (n=4462)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8815 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.201 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6028` → IC=+0.186 (n=3207)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6028 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2343.73` → IC=+0.172 (n=6672)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2343.73 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.194 (n=7624)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 87.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.191 (n=6052)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.007 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1487` → IC=+0.188 (n=3994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1487 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5655` → IC=+0.238 (n=9072)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5655 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2493` → IC=+0.162 (n=5637)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2493 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.034` → IC=+0.203 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.034 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.182 (n=8775)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.161 (n=2743)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.705 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.244 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6301` → IC=+0.192 (n=2774)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6301 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.192 (n=5352)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 48.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.208 (n=567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.225 (n=568)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3602` → IC=+0.191 (n=1699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3602 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=1152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.541` → IC=+0.345 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.541 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.258 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.5477` → IC=+0.185 (n=706)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5477 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2431` → IC=+0.197 (n=727)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2431 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=1026)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.262 (n=1186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1298` → IC=+0.284 (n=585)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1298 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=1217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3485` → IC=+0.290 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3485 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.537` → IC=+0.263 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.537 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.283 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.5466` → IC=+0.257 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5466 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6339` → IC=+0.279 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6339 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1801.6295` → IC=+0.262 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1801.6295 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.191 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0848` → IC=+0.163 (n=535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0848 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3107` → IC=+0.203 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3107 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.3445` → IC=+0.195 (n=647)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3445 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.169 (n=367)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.251` → IC=+0.154 (n=1442)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.251 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6305` → IC=+0.180 (n=535)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6305 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.206 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1166` → IC=+0.163 (n=1363)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.1166 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7596` → IC=+0.155 (n=1032)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7596 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `15748.4784` → IC=+0.158 (n=727)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 15748.4784 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `476.0` → IC=+0.159 (n=1482)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 476.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2581` → IC=+0.165 (n=1220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2581 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.6545` → IC=+0.195 (n=1386)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6545 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.5361` → IC=+0.151 (n=299)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.5361 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1343` → IC=+0.166 (n=1253)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1343 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.161 (n=234)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.162 (n=1386)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1954 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1513` → IC=+0.199 (n=373)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1513 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4038` → IC=+0.160 (n=1288)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4038 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.0873` → IC=+0.164 (n=584)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.0873 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `421.0` → IC=+0.158 (n=1048)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 421.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.247 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=1696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1651)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6709` → IC=+0.257 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6709 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.811` → IC=+0.294 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.811 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.212` → IC=+0.222 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.212 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8378` → IC=+0.241 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8378 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.238 (n=1511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1667` → IC=+0.235 (n=665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1667 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.3594` → IC=+0.269 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3594 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.766` → IC=+0.278 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.766 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.304 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7564` → IC=+0.233 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7564 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1919` → IC=+0.237 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1919 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1884.1532` → IC=+0.245 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1884.1532 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.230 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.179 (n=568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0035 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4387` → IC=+0.145 (n=1704)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4387 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=1782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.261 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.877 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3736` → IC=+0.163 (n=669)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3736 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.201` → IC=+0.161 (n=709)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.201 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8764` → IC=+0.155 (n=1136)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8764 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2375` → IC=+0.214 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2375 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.150 (n=726)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.768` → IC=+0.150 (n=1099)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.768 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `8015.433` → IC=+0.233 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8015.433 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.148 (n=529)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 79.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.163 (n=1224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0066 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4484` → IC=+0.154 (n=1390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4484 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7022` → IC=+0.184 (n=1390)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7022 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.6022` → IC=+0.143 (n=1543)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.6022 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.181 (n=205)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6962` → IC=+0.150 (n=612)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6962 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1938` → IC=+0.144 (n=464)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1938 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.29` → IC=+0.261 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.29 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.151 (n=1318)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10905.3195` → IC=+0.210 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10905.3195 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.146 (n=1319)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 179.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.138 (n=1129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0081 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.190 (n=1696)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4706 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0792` → IC=+0.201 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0792 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.485` → IC=+0.233 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.485 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8936` → IC=+0.134 (n=1129)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8936 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1702)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.248 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.130 (n=1304)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 54.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.175 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1331` → IC=+0.158 (n=551)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1331 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=1707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.204 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.131 (n=1352)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.486` → IC=+0.124 (n=1597)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.486 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.717` → IC=+0.153 (n=727)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.717 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.167 (n=256)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4462` → IC=+0.143 (n=497)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4462 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.4991` → IC=+0.125 (n=497)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4991 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2848.7898` → IC=+0.169 (n=550)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2848.7898 (IC base=+0.112)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0193` → IC=+0.218 (n=1129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0193 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=1519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.250 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.2024` → IC=+0.233 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2024 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.285` → IC=+0.270 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.285 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.0683` → IC=+0.212 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0683 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6395` → IC=+0.215 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6395 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.235` → IC=+0.248 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.235 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.5093` → IC=+0.239 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5093 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2626.1883` → IC=+0.220 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2626.1883 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.228 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.009 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.220 (n=604)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.208 (n=1274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5183` → IC=+0.254 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5183 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.9236` → IC=+0.203 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9236 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.834` → IC=+0.258 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.834 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.232 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.266 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2023` → IC=+0.195 (n=1431)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2023 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.195 (n=1626)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=3025)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.158 (n=2539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0092 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.152 (n=2576)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0056 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.5229` → IC=+0.160 (n=2884)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5229 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.164 (n=1285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.212 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1868` → IC=+0.160 (n=1053)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1868 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.4904` → IC=+0.145 (n=1767)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4904 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.187` → IC=+0.176 (n=473)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.187 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.9001` → IC=+0.160 (n=1248)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.9001 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.172` → IC=+0.184 (n=789)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.172 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4583` → IC=+0.158 (n=951)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4583 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.8856` → IC=+0.162 (n=1899)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8856 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `8269.6944` → IC=+0.155 (n=1307)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8269.6944 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=764)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.156 (n=2282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.163 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.184` → IC=+0.170 (n=1004)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.184 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6922` → IC=+0.151 (n=433)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6922 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.4314` → IC=+0.131 (n=2263)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4314 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.281` → IC=+0.148 (n=2271)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.281 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2467` → IC=+0.143 (n=2179)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2467 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.0971` → IC=+0.140 (n=2064)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.0971 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2204` → IC=+0.144 (n=487)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2204 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4255` → IC=+0.152 (n=751)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4255 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8136` → IC=+0.141 (n=1501)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8136 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=3025)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7149.4539` → IC=+0.151 (n=2037)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7149.4539 (IC base=+0.137)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.173 (n=338)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0056 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.179 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0065 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0895` → IC=+0.192 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0895 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.156 (n=361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.5544` → IC=+0.182 (n=256)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5544 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2158` → IC=+0.163 (n=182)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.2158 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.3825` → IC=+0.160 (n=372)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.3825 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.403` → IC=+0.168 (n=407)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 2.403 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.2549` → IC=+0.162 (n=383)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2549 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.8487` → IC=+0.189 (n=255)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.8487 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.3075` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3075 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.6734` → IC=+0.208 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6734 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `12505.1299` → IC=+0.198 (n=342)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 12505.1299 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.212 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0847` → IC=+0.174 (n=311)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0847 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.177 (n=410)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.138 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.141 (n=422)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6091 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6994` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6994 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.219` → IC=+0.139 (n=950)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.219 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.111` → IC=+0.153 (n=1019)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 9.111 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.185 (n=621)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8811 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.164 (n=436)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.147 (n=310)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.147 (n=619)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `11396.4572` → IC=+0.152 (n=931)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11396.4572 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `706.0` → IC=+0.145 (n=886)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 706.0 (IC base=+0.138)

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
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.154 (n=802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0073 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.163 (n=911)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0044 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3878` → IC=+0.157 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3878 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.165 (n=317)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.5636` → IC=+0.157 (n=608)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5636 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.7903` → IC=+0.168 (n=413)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.7903 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9629` → IC=+0.159 (n=203)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.9629 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.4255` → IC=+0.164 (n=855)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.4255 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.676` → IC=+0.163 (n=912)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.676 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.0865` → IC=+0.157 (n=802)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0865 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.7179` → IC=+0.157 (n=814)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7179 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1099` → IC=+0.156 (n=841)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1099 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.161 (n=393)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.167 (n=298)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=901)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=680)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3967` → IC=+0.170 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3967 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.154 (n=521)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.143 (n=774)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7466 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.0998` → IC=+0.148 (n=773)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.0998 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.9113` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.9113 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.3872` → IC=+0.140 (n=792)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3872 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.376` → IC=+0.147 (n=701)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.376 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6464` → IC=+0.177 (n=258)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6464 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.166 (n=327)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.156 (n=667)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7829` → IC=+0.145 (n=505)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7829 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7578.204` → IC=+0.166 (n=773)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7578.204 (IC base=+0.140)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `0.5469` → IC=+0.143 (n=225)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.5469 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1868` → IC=+0.128 (n=154)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.1868 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.247` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.247 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `1.4231` → IC=+0.121 (n=217)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.4231 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `3421.4081` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3421.4081 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.142 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0068 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.3995` → IC=+0.151 (n=144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3995 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.162 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 10.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.5969` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.5969 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.699` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.699 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` < `0.092` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.092 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.8499` → IC=+0.127 (n=140)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8499 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3291.3893` → IC=+0.138 (n=216)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3291.3893 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.152 (n=205)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 60.0 (IC base=+0.109)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.207 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=366)

- **FILTRO** `dist_vwap_pct` > `0.1862` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1862
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=319)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.194 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0041 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.130 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.208 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1543` → IC=+0.161 (n=444)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1543 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.443` → IC=+0.206 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.443 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.0912` → IC=+0.137 (n=624)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.0912 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=661)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2424.4386` → IC=+0.143 (n=362)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2424.4386 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.057` → IC=+0.269 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.057 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.0685` → IC=+0.203 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0685 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.125 (n=230)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.003)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.162 (n=312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.006 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.5161` → IC=+0.189 (n=281)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5161 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1366` → IC=+0.185 (n=147)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1366 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.0669` → IC=+0.127 (n=247)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0669 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` < `0.0677` → IC=+0.138 (n=216)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.0677 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.174 (n=213)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=293)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `3653.1061` → IC=+0.122 (n=178)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3653.1061 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.082` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.082 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.5944` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.5944 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.9323` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.9323 (IC base=+0.050)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=116)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=117)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.181 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.004 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.3477` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3477 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.853` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.853 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `0.9325` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.9325 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.7281` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7281 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=185)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `1748.9026` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1748.9026 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=-0.019)

- **PATRÓN** `dist_vwap_pct` < `0.1283` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1283 (IC base=-0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.956` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.956 (IC base=-0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` > `2.268` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.268 (IC base=-0.019)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=-0.019)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.271 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=91)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=64)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.133 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 13.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.6731` → IC=+0.182 (n=234)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6731 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.438` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.438 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.0643 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.075)

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
- **FILTRO** `hora_utc` > `9.0` → IC=-0.396 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=153)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=183)

- **FILTRO** `volumen_regimen` < `0.7506` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7506
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=134)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=114)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=149)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=69)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `ibs_20min` < `0.0648` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0648
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=47)

- **FILTRO** `volumen_spike_ratio` > `3.7991` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7991
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

- **FILTRO** `sigma_h` < `0.0017` → IC=-0.289 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=54)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=25)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=54)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8831` → IC=-0.411 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8831
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=38)

- **FILTRO** `ibs_20min` > `0.6404` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6404
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `dist_vwap_pct` < `0.2294` → IC=-0.276 (n=47)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2294
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.221)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.441 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=47)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.123 (n=120)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=234)

- **FILTRO** `dist_vwap_pct` > `0.4433` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4433
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=316)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.161 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0058 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.145 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.165 (n=252)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.6522 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.4967` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.4967 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` < `0.1654` → IC=+0.124 (n=147)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1654 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.1906` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.1906 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.944` → IC=+0.140 (n=109)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 5.944 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.159 (n=121)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.048)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.576` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.576
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=82)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=82)

- **PATRÓN** `drift_60min` |x|≤ `0.2204` → IC=+0.157 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2204 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.113` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.113 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.3016` → IC=+0.122 (n=146)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.3016 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` < `0.1813` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1813 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.8706` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.8706 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.114)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=75)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.151 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0045 (IC base=+0.063)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.121 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.063)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.6645` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6645 (IC base=+0.063)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.013)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.210 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.226 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.223 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.7027` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7027 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.284 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.201)

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
- **PATRÓN** `libro_liquidez` > `2919.1618` → IC=+0.174 (n=234)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2919.1618 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2919.1618` → IC=+0.174 (n=234)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2919.1618 (IC base=+0.105)

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
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=209)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=195)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1765)

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
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=127)

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

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.024)

- **PATRÓN** `liq_usd_total` > `68754.71` → IC=+0.170 (n=95)

  - _Acción_: Kelly boost +0.85€ cuando `liq_usd_total` > 68754.71 (IC base=+0.024)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=779)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=733)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=428)

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
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=152)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=-0.018)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=627)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=627)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=499)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=354)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=354)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.148 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=283)

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

- **FILTRO** `hora_utc` > `9.0` → IC=-0.132 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=45)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=104)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=202)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=82)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=85)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=238)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=238)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=128)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.42` → IC=-0.169 (n=243)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=277)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.130 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=268)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.183 (n=137)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.47 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.048)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.59 (IC base=+0.125)

- **PATRÓN** `restante_min` > `3.82` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 3.82 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `lag_apertura_s` < `60.77` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `lag_apertura_s` < 60.77 (IC base=+0.125)

- **PATRÓN** `profundidad_ratio` > `79.6` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio` > 79.6 (IC base=+0.125)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` > `11.54` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `restante_min` > 11.54
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=28)

- **FILTRO** `profundidad_ratio` < `56.2` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.2
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `restante_min` < `13.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `restante_min` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.220 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **FILTRO** `lag_apertura_s` > `126.34` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `lag_apertura_s` > 126.34
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=24)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `restante_min` < `3.44` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `restante_min` < 3.44
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.231 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `lag_apertura_s` > `71.83` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `lag_apertura_s` > 71.83
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=26)

- **FILTRO** `profundidad_ratio` < `26.3` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `profundidad_ratio` < 26.3
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **PATRÓN** `profundidad_ratio` > `26.3` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `profundidad_ratio` > 26.3 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.48` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **FILTRO** `lag_apertura_s` > `90.99` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.99
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **PATRÓN** `restante_min` > `12.42` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 12.42 (IC base=-0.011)

- **PATRÓN** `lag_apertura_s` < `154.62` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 154.62 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` > `0.42` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=12)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=22)

- **FILTRO** `profundidad_ratio` < `26.5` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `profundidad_ratio` < 26.5
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=42)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.241 (n=52)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `restante_min` < `2.74` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 2.74
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `lag_apertura_s` > `135.64` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 135.64
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `profundidad_ratio` < `26.9` → IC=-0.161 (n=54)

  - _Acción_: SKIP cuando `profundidad_ratio` < 26.9
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=39)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7498)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.165 (n=3501)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=10573)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.167 (n=3633)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=10921)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.209 (n=599)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1843)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.153 (n=643)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=1965)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.189 (n=612)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1874)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=637)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=1968)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.172 (n=599)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1829)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=636)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1970)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2761)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=2935)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2941)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` > `0.1705` → IC=-0.146 (n=125)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1705
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=377)

- **FILTRO** `libro_liquidez` < `17311.9684` → IC=-0.123 (n=165)

  - _Acción_: SKIP cuando `libro_liquidez` < 17311.9684
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=337)

- **FILTRO** `libro_liquidez` < `16979.4809` → IC=-0.145 (n=226)

  - _Acción_: SKIP cuando `libro_liquidez` < 16979.4809
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=680)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.204 (n=79)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=237)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=239)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `py_entrada` < `0.415` → IC=-0.214 (n=197)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=591)

- **FILTRO** `drift_20min_pct` |x|> `0.2312` → IC=-0.122 (n=300)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2312
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=585)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=9940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=22273)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=7870)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=24343)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.235 (n=8041)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=24172)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=10943)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=21270)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9929)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=30484)

- **FILTRO** `ibs_7min` > `0.2929` → IC=-0.178 (n=10101)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2929
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=30312)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=1628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3703)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1273)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4058)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.249 (n=1759)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3572)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.185 (n=1225)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4106)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.261 (n=1714)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=5226)

- **FILTRO** `drift_7min_pct` |x|> `0.1124` → IC=-0.126 (n=2359)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1124
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4581)

- **FILTRO** `ibs_7min` > `0.7895` → IC=-0.206 (n=1734)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7895
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=5206)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4262)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1343)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4218)

- **FILTRO** `ibs_7min` < `0.7478` → IC=-0.193 (n=1390)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7478
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4171)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.175 (n=1388)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4173)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.253 (n=1411)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4239)

- **FILTRO** `ibs_7min` > `0.2601` → IC=-0.176 (n=1412)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2601
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4238)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.182 (n=1411)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4239)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=1240)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3820)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.305 (n=1242)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3818)

- **FILTRO** `ibs_7min` < `0.1935` → IC=-0.258 (n=1260)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3800)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.219 (n=1173)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3887)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.237 (n=1698)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=5728)

- **FILTRO** `ibs_7min` > `0.7456` → IC=-0.174 (n=1856)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7456
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=5570)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=3606)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.231 (n=1569)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3742)

- **FILTRO** `ibs_7min` < `0.7412` → IC=-0.181 (n=1327)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7412
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3984)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.170 (n=1306)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4005)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=1204)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4223)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.176 (n=1356)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4071)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.183 (n=1344)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4083)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.257 (n=1364)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4251)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.239 (n=1397)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4218)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1835)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5851)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.254 (n=1720)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3615)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.227 (n=1321)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=4014)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1298)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4037)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.205 (n=1742)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=5542)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1077)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=531)

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
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=556)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.126 (n=739)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.63€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.111)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.139 (n=247)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 469.512 (IC base=+0.111)

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
- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 12.0 (IC base=+0.093)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.170 (n=101)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.086)

- **PATRÓN** `total_vol_5m` < `394.71` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 394.71 (IC base=+0.086)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.172 (n=129)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 6300.756 (IC base=+0.132)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.149 (n=129)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.136 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 13.0 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `263476.4` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 263476.4 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3566.692` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3566.692 (IC base=+0.104)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.007` → IC=-0.326 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=253)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0073` → IC=-0.381 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=80)

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

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.321 (n=82)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=246)

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
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=176)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=295)

- **FILTRO** `streak_estiramiento` > `0.8486` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8486
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=191)

- **PATRÓN** `streak_estiramiento` < `0.4086` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.4086 (IC base=+0.029)

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
- **FILTRO** `streak_estiramiento` > `0.5576` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5576
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=32)

- **FILTRO** `ballena_activa_n` > `52.0` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 52.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=34)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=-0.009)

- **PATRÓN** `streak_estiramiento` < `0.5576` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.5576 (IC base=-0.009)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.120 (n=77)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 49.0 (IC base=+0.055)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=90)

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
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=781)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=787)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=395)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=598)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=752)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=721)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2901)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1474)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1482)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.220 (n=723)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0509` → IC=+0.204 (n=532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0509 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2136` → IC=+0.195 (n=533)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.2136 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1251` → IC=+0.232 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1251 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=1489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6061` → IC=+0.266 (n=1593)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6061 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.1594` → IC=+0.189 (n=728)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1594 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.6143` → IC=+0.178 (n=1532)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.6143 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.771` → IC=+0.279 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.771 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2975.4354` → IC=+0.195 (n=1062)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2975.4354 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=608)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.218 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.297 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.256 (n=121)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.207)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.273 (n=363)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.4048` → IC=+0.255 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4048 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.270 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.248 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.207)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `24.537` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 24.537
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=371)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.151 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.160 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0051 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.151 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2337` → IC=+0.175 (n=124)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2337 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.258` → IC=+0.159 (n=265)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.258 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.6603` → IC=+0.252 (n=332)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6603 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5915` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.5915 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1631` → IC=+0.152 (n=294)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1631 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.19` → IC=+0.201 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.19 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `9475.4181` → IC=+0.161 (n=169)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9475.4181 (IC base=+0.136)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.144 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=84)

- **FILTRO** `ibs_15` > `0.2172` → IC=-0.258 (n=31)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2172
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=96)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.300 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.210 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0701` → IC=+0.202 (n=169)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0701 (IC base=+0.173)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.232 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.209 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.173)

- **PATRÓN** `ibs_15` > `0.6122` → IC=+0.259 (n=189)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6122 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.203 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.122 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=144)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `3074.7539` → IC=+0.284 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3074.7539 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.228 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.173)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5695` → IC=-0.135 (n=124)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5695
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=901)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=+0.008)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0176` → IC=+0.234 (n=280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0176 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0864` → IC=+0.211 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0864 (IC base=+0.187)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0393` → IC=+0.192 (n=420)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0393 (IC base=+0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0883` → IC=+0.245 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0883 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.229 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.187)

- **PATRÓN** `ibs_15` > `0.5488` → IC=+0.282 (n=420)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5488 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.213 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.8385` → IC=+0.187 (n=487)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.8385 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.92` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.92 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.785` → IC=+0.189 (n=419)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 10.785 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `2915.737` → IC=+0.282 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2915.737 (IC base=+0.187)

- **PATRÓN** `ibs_15` < `0.1171` → IC=+0.160 (n=471)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1171 (IC base=+0.048)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.341 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.339)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.378 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.339)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.348 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.339)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.365 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.339)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.376 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.339)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.385 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.339)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.384 (n=410)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.339)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.386 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.339)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.340 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.339)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.143` → IC=+0.344 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.143 (IC base=+0.339)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.729` → IC=+0.340 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.729 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.354 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.339)

- **PATRÓN** `ballena_activa_n` < `463.0` → IC=+0.361 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 463.0 (IC base=+0.339)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.352 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.372 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.343)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.373 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.343)

- **PATRÓN** `drift_15min` |x|≤ `0.4288` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4288 (IC base=+0.343)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.352 (n=228)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.343)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.385 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.370 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.343)

- **PATRÓN** `ibs_15` > `0.8166` → IC=+0.378 (n=228)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8166 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.347 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `15821.8878` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15821.8878 (IC base=+0.343)

- **PATRÓN** `ballena_activa_n` < `574.0` → IC=+0.390 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 574.0 (IC base=+0.343)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.384 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.347 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.354 (n=163)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2929` → IC=+0.361 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2929 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.395 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.7401` → IC=+0.391 (n=182)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7401 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` < `0.1227` → IC=+0.341 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1227 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.335 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.332)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `3532.3524` → IC=+0.354 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3532.3524 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.344 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.332)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.218 (n=654)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1966)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.191 (n=888)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1732)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.255 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.060)

- **PATRÓN** `ibs_15` > `0.6371` → IC=+0.274 (n=627)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6371 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.2788` → IC=+0.186 (n=498)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.2788 (IC base=-0.060)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1206` → IC=+0.247 (n=1159)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1206 (IC base=-0.034)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.177` → IC=+0.235 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.177 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3452` → IC=+0.279 (n=1738)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3452 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `0.6912` → IC=+0.295 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6912 (IC base=-0.034)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.223 (n=399)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1201)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.231 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1200)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.210 (n=1015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=585)

- **FILTRO** `sigma_ewma_delta_pct` > `19.843` → IC=-0.249 (n=289)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.843
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1311)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.165 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0029 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.287 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.084)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.324 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.084)

- **PATRÓN** `ibs_15` > `0.7466` → IC=+0.328 (n=172)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7466 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.283 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.282 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.084)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6675` → IC=-0.193 (n=99)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6675
  - _Potencial_: sin este filtro IC_bueno=+0.267 (n=299)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.166 (n=381)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.197 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0051 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.216 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.152)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.152)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.162 (n=199)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.239 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.267 (n=299)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1187` → IC=+0.187 (n=215)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1187 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.857` → IC=+0.165 (n=237)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.857 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=381)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `10970.2258` → IC=+0.196 (n=136)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 10970.2258 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.265 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.4447` → IC=+0.227 (n=682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4447 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `0.7897` → IC=+0.231 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7897 (IC base=+0.226)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2036` → IC=+0.259 (n=309)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2036 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.238 (n=303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.226)

- **PATRÓN** `ibs_15` < `0.3453` → IC=+0.266 (n=682)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3453 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.7773` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7773 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.718` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.718 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.189` → IC=+0.234 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.189 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3551.8492` → IC=+0.226 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.8492 (IC base=+0.226)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.244 (n=154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=464)

- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.217 (n=210)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=408)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.263 (n=154)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=464)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.168)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.230 (n=276)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.269 (n=309)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.4921` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4921 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.2005` → IC=+0.226 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2005 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.259 (n=384)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=385)

- **FILTRO** `drift_15min` |x|> `1.2489` → IC=-0.263 (n=192)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2489
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=577)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.262 (n=187)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=582)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1326` → IC=+0.280 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1326 (IC base=-0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1028` → IC=+0.337 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1028 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3429` → IC=+0.307 (n=464)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3429 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.9013` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9013 (IC base=-0.044)

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
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.298 (n=438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.293 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.328 (n=219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.315 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.348 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.329 (n=657)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.1575` → IC=+0.321 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1575 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.331 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.296 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `14611.6311` → IC=+0.310 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14611.6311 (IC base=+0.294)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.300 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.290 (n=165)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.347 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.313 (n=121)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3807` → IC=+0.308 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3807 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.305 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.317 (n=364)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.444` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.444 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.357 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.331 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.310 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.301)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.304 (n=197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.301)

- **PATRÓN** `delta_ratio_macro` |x|> `0.226` → IC=+0.320 (n=98)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.226 (IC base=+0.301)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.339 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.334 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.301)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.341 (n=293)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.302 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.321 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.312 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.301)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2593` → IC=-0.176 (n=69)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2593
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=208)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1132` → IC=-0.176 (n=69)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1132
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=208)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.173 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=331)

- **FILTRO** `drift_15min` |x|> `0.5254` → IC=-0.140 (n=109)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5254
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=330)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1445` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=108)

- **FILTRO** `sigma_h` < `0.0053` → IC=-0.167 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2228` → IC=-0.259 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2228
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
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `drift_15min` |x|> `0.1344` → IC=-0.241 (n=25)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1344
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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

- **PATRÓN** `T_h` < `111.9957` → IC=+0.292 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9957 (IC base=+0.281)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6061 sube el IC de +0.186 a +0.266 en UPDOWN_GBM#15min (n=1593). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.207 a +0.273 en UPDOWN_GBM#BTC#15min (n=363). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6603 sube el IC de +0.136 a +0.252 en UPDOWN_GBM#ETH#15min (n=332). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6122 sube el IC de +0.173 a +0.259 en UPDOWN_GBM#SOL#15min (n=189). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5488 sube el IC de +0.187 a +0.282 en UPDOWN_GBM#XRP#15min (n=420). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1171 sube el IC de +0.048 a +0.160 en UPDOWN_GBM#XRP#15min (n=471). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6371 sube el IC de -0.060 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3452 sube el IC de -0.034 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1738). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7466 sube el IC de +0.084 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=172). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.152 a +0.267 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3453 sube el IC de +0.226 a +0.266 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=682). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.168 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.042 a +0.269 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=309). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3429 sube el IC de -0.044 a +0.307 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=464). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.294 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=657). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.286 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=364). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.301 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=293). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.339 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=410). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8166 sube el IC de +0.343 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=228). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7401 sube el IC de +0.332 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=182). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1321 | +0.098 | +193.26€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1321 | +0.098 | +193.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 984 | +0.107 | +167.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 984 | +0.107 | +167.20€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 251 | +0.053 | +7.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 251 | +0.053 | +7.40€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 28146 | -0.091 | -3804.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1451 | -0.049 | -220.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 26695 | -0.094 | -3584.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3687 | -0.092 | -589.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3687 | -0.092 | -589.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1451 | -0.049 | -220.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1451 | -0.049 | -220.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3466 | -0.096 | -781.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3466 | -0.096 | -781.14€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7241 | -0.024 | -678.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7241 | -0.024 | -678.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6757 | -0.097 | -454.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6757 | -0.097 | -454.72€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5544 | -0.180 | -1080.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5544 | -0.180 | -1080.43€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 18047 | -0.028 | +4050.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4715 | -0.000 | +1824.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 13332 | -0.038 | +2226.16€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 18047 | -0.028 | +4050.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4715 | -0.000 | +1824.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 13332 | -0.038 | +2226.16€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1474 | -0.102 | -187.69€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1306 | -0.109 | -166.33€ | 0 | 0 |
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
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 62 | -0.172 | -6.21€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 62 | -0.172 | -6.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 92433 | +0.112 | -4730.29€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13967 | +0.185 | -435.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 371 | -0.085 | -51.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 72074 | +0.099 | -4024.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6021 | +0.107 | -218.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11988 | +0.098 | -1022.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 45 | -0.160 | -0.32€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11928 | +0.099 | -1010.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 18694 | +0.131 | -375.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4394 | +0.203 | -134.25€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11950 | +0.111 | -196.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2308 | +0.104 | -22.01€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 12029 | +0.088 | -1131.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 52 | -0.093 | -6.98€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11962 | +0.090 | -1113.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 19674 | +0.123 | -405.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5407 | +0.175 | -87.18€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 12076 | +0.105 | -252.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2179 | +0.097 | -56.62€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 18047 | +0.113 | -1078.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4023 | +0.188 | -216.45€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 274 | -0.043 | +2.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 12216 | +0.091 | -724.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1534 | +0.125 | -140.06€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12001 | +0.100 | -716.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 46 | -0.021 | +9.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11942 | +0.101 | -725.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14669 | +0.192 | -962.08€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14669 | +0.192 | -962.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3498 | +0.168 | -366.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3498 | +0.168 | -366.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1209 | +0.198 | -6.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1209 | +0.198 | -6.75€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3442 | +0.179 | -298.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3442 | +0.179 | -298.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3063 | +0.239 | -97.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3063 | +0.239 | -97.81€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3378 | +0.192 | -206.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3378 | +0.192 | -206.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 688 | +0.429 | -20.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 688 | +0.429 | -20.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 264 | +0.436 | -3.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 264 | +0.436 | -3.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 259 | +0.435 | -3.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 259 | +0.435 | -3.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 156 | +0.405 | -10.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 156 | +0.405 | -10.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 50497 | +0.197 | -4013.51€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 50497 | +0.197 | -4013.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8740 | +0.176 | -1020.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8740 | +0.176 | -1020.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8063 | +0.221 | -314.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8063 | +0.221 | -314.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8718 | +0.171 | -1057.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8718 | +0.171 | -1057.74€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8162 | +0.218 | -324.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8162 | +0.218 | -324.90€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8342 | +0.203 | -557.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8342 | +0.203 | -557.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8472 | +0.193 | -737.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8472 | +0.193 | -737.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 19036 | +0.118 | +182.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 19036 | +0.118 | +182.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9451 | +0.123 | +159.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9451 | +0.123 | +159.88€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9585 | +0.113 | +22.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9585 | +0.113 | +22.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1463 | +0.292 | -8.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1463 | +0.292 | -8.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 652 | +0.278 | -16.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 652 | +0.278 | -16.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 703 | +0.294 | +4.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 703 | +0.294 | +4.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 108 | +0.345 | +3.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 108 | +0.345 | +3.06€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 643 | +0.436 | -2.27€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 643 | +0.436 | -2.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 303 | +0.434 | -2.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 303 | +0.434 | -2.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 297 | +0.440 | +0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 297 | +0.440 | +0.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 43 | +0.389 | +0.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 43 | +0.389 | +0.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1109 | +0.076 | -40.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 384 | +0.062 | -29.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 725 | +0.083 | -11.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 875 | +0.083 | -15.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 150 | +0.079 | -4.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 725 | +0.083 | -11.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 173 | +0.026 | -28.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 173 | +0.026 | -28.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 35275 | +0.096 | -1125.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2917 | +0.089 | +16.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 32358 | +0.097 | -1141.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 19819 | +0.101 | -339.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2917 | +0.089 | +16.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 16902 | +0.103 | -355.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6615 | +0.106 | -45.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6615 | +0.106 | -45.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8841 | +0.079 | -740.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8841 | +0.079 | -740.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 803 | +0.215 | -96.34€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 803 | +0.215 | -96.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 803 | +0.215 | -96.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 803 | +0.215 | -96.34€ | 2 | 4 |
| ✅ GBM_LATE_15M | 25322 | +0.082 | +11976.09€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 25322 | +0.082 | +11976.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4233 | +0.193 | +3069.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4233 | +0.193 | +3069.06€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 3755 | +0.177 | +2604.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3755 | +0.177 | +2604.49€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 4399 | +0.198 | +3280.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4399 | +0.198 | +3280.83€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3740 | +0.020 | +787.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3740 | +0.020 | +787.89€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 3627 | -0.033 | +822.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3627 | -0.033 | +822.35€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 5568 | -0.041 | +1411.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5568 | -0.041 | +1411.48€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 26751 | +0.085 | +13908.96€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 26751 | +0.085 | +13908.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5071 | +0.017 | +2676.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5071 | +0.017 | +2676.95€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5572 | +0.015 | +1149.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5572 | +0.015 | +1149.40€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3803 | +0.261 | +3811.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3803 | +0.261 | +3811.76€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4340 | +0.003 | +816.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4340 | +0.003 | +816.06€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4349 | +0.027 | +1626.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4349 | +0.027 | +1626.42€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3616 | +0.274 | +3828.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3616 | +0.274 | +3828.37€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 20412 | +0.167 | +15167.73€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 20412 | +0.167 | +15167.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3074 | +0.206 | +2433.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3074 | +0.206 | +2433.62€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3247 | +0.148 | +2372.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3247 | +0.148 | +2372.80€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3204 | +0.206 | +2529.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3204 | +0.206 | +2529.92€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3429 | +0.133 | +2372.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3429 | +0.133 | +2372.79€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3795 | +0.116 | +2580.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3795 | +0.116 | +2580.95€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3663 | +0.203 | +2877.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3663 | +0.203 | +2877.65€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5093 | +0.128 | +2143.39€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5093 | +0.128 | +2143.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 189 | +0.123 | +84.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 189 | +0.123 | +84.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1457 | +0.123 | +657.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1457 | +0.123 | +657.88€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1494 | +0.143 | +662.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1494 | +0.143 | +662.71€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1076 | +0.103 | +344.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1076 | +0.103 | +344.94€ | 1 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 25439 | +0.175 | +18845.45€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 25439 | +0.175 | +18845.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4034 | +0.220 | +3391.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4034 | +0.220 | +3391.54€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3984 | +0.150 | +2626.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3984 | +0.150 | +2626.50€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4171 | +0.225 | +3587.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4171 | +0.225 | +3587.05€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4124 | +0.137 | +2799.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4124 | +0.137 | +2799.66€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4457 | +0.112 | +2789.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4457 | +0.112 | +2789.56€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4669 | +0.204 | +3651.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4669 | +0.204 | +3651.14€ | 0 | 23 |
| ✅ GBM_LATE_5M | 6884 | +0.145 | +3870.37€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 6884 | +0.145 | +3870.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1751 | +0.143 | +1131.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1751 | +0.143 | +1131.76€ | 0 | 30 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2244 | +0.147 | +1241.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2244 | +0.147 | +1241.59€ | 0 | 30 |
| ✅ GBM_LATE_5M#SOL | 586 | +0.099 | +197.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 586 | +0.099 | +197.59€ | 0 | 16 |
| ✅ GBM_LATE_5M#XRP | 820 | +0.116 | +318.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 820 | +0.116 | +318.37€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1703 | +0.070 | +742.65€ | 2 | 12 |
| ✅ GBM_LATE_60M#60min | 1703 | +0.070 | +742.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 613 | +0.089 | +260.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 613 | +0.089 | +260.25€ | 0 | 15 |
| ✅ GBM_LATE_60M#ETH | 564 | +0.072 | +290.95€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 564 | +0.072 | +290.95€ | 2 | 16 |
| ✅ GBM_LATE_60M#SOL | 526 | +0.045 | +191.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 526 | +0.045 | +191.45€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 369 | -0.257 | -25.96€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 369 | -0.257 | -25.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 141 | -0.227 | -11.75€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 141 | -0.227 | -11.75€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 122 | -0.250 | -6.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 122 | -0.250 | -6.90€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 106 | -0.296 | -7.30€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 106 | -0.296 | -7.30€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 690 | +0.071 | +149.37€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 690 | +0.071 | +149.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 270 | +0.059 | +46.83€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 270 | +0.059 | +46.83€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 198 | +0.035 | +8.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 198 | +0.035 | +8.84€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 222 | +0.116 | +93.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 222 | +0.116 | +93.71€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 98 | +0.260 | +81.48€ | 0 | 9 |
| ✅ LATE_WINDOW_5MIN#5min | 98 | +0.260 | +81.48€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 98 | +0.260 | +81.48€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 98 | +0.260 | +81.48€ | 0 | 9 |
| ✅ LEADLAG_BTC_XRP_15M | 1920 | +0.098 | +515.18€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1920 | +0.098 | +515.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1920 | +0.098 | +515.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1920 | +0.098 | +515.18€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 379 | -0.077 | -33.28€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 379 | -0.077 | -33.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 96 | -0.061 | -5.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 96 | -0.061 | -5.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 135 | -0.018 | -3.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 135 | -0.018 | -3.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1963 | +0.006 | +15.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1963 | +0.006 | +15.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 104 | +0.019 | -1.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 104 | +0.019 | -1.14€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 223 | -0.007 | +10.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 223 | -0.007 | +10.32€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 161 | -0.034 | -6.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 161 | -0.034 | -6.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 826 | +0.028 | +24.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 826 | +0.028 | +24.18€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 468 | +0.000 | -4.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 468 | +0.000 | -4.94€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 181 | -0.030 | -6.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 181 | -0.030 | -6.21€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1076 | -0.044 | -26.60€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1076 | -0.044 | -26.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 306 | -0.042 | -12.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 306 | -0.042 | -12.94€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 359 | -0.026 | -0.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 359 | -0.026 | -0.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 411 | -0.059 | -12.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 411 | -0.059 | -12.69€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 1055 | -0.040 | -26.05€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 493 | -0.045 | -18.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 562 | -0.035 | -7.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 33 | -0.014 | +2.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 19 | +0.023 | +1.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 14 | -0.044 | +0.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 263 | +0.040 | +40.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 119 | +0.012 | +9.80€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 144 | +0.062 | +30.77€ | 0 | 5 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 159 | -0.071 | -13.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 75 | -0.058 | -5.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 84 | -0.081 | -8.35€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 189 | -0.086 | -23.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 87 | -0.084 | -8.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 102 | -0.086 | -14.58€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 164 | -0.042 | -6.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 85 | -0.040 | -1.22€ | 2 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 79 | -0.043 | -5.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 247 | -0.070 | -25.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 108 | -0.082 | -14.21€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 139 | -0.060 | -10.78€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M | 14362 | -0.012 | -207.62€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14362 | -0.012 | -207.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3079 | -0.021 | -60.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3079 | -0.021 | -60.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 28628 | -0.006 | +1313.23€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 28628 | -0.006 | +1313.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5050 | +0.017 | +619.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5050 | +0.017 | +619.36€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4445 | -0.027 | -48.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4445 | -0.027 | -48.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5091 | +0.015 | +476.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5091 | +0.015 | +476.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4220 | -0.051 | -136.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4220 | -0.051 | -136.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4788 | -0.010 | +181.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4788 | -0.010 | +181.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5034 | +0.008 | +220.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5034 | +0.008 | +220.66€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5797 | -0.057 | -130.42€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5797 | -0.057 | -130.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1204 | +0.001 | -14.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1204 | +0.001 | -14.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1408 | -0.081 | -36.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1408 | -0.081 | -36.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 621 | -0.112 | -17.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 621 | -0.112 | -17.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1673 | -0.076 | -30.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1673 | -0.076 | -30.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 72626 | -0.072 | +1772.46€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 72626 | -0.072 | +1772.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 12271 | -0.079 | +734.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 12271 | -0.079 | +734.80€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 11211 | -0.092 | -476.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 11211 | -0.092 | -476.64€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 12486 | -0.066 | +718.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 12486 | -0.066 | +718.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10738 | -0.093 | -159.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10738 | -0.093 | -159.13€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 13301 | -0.048 | +383.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 13301 | -0.048 | +383.19€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12619 | -0.063 | +571.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12619 | -0.063 | +571.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7588 | -0.024 | -116.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7588 | -0.024 | -116.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1669 | -0.027 | -2.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1669 | -0.027 | -2.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2146 | -0.019 | -24.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2146 | -0.019 | -24.82€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1036 | -0.041 | -14.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1036 | -0.041 | -14.97€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1120 | +0.104 | +361.50€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 984 | +0.111 | +348.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 229 | +0.132 | +109.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 229 | +0.132 | +109.02€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 192 | +0.093 | +44.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 192 | +0.093 | +44.00€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 201 | +0.086 | +59.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 201 | +0.086 | +59.80€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#SOL | 172 | +0.132 | +78.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 172 | +0.132 | +78.55€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 190 | +0.104 | +57.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 190 | +0.104 | +57.54€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 469 | -0.063 | -57.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 469 | -0.063 | -57.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 101 | -0.015 | +1.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 101 | -0.015 | +1.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 57 | -0.127 | -16.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 57 | -0.127 | -16.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 140 | -0.085 | -27.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 140 | -0.085 | -27.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 97 | -0.005 | -0.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 97 | -0.005 | -0.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 74 | -0.105 | -14.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 74 | -0.105 | -14.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 568 | -0.103 | -43.94€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 261 | -0.158 | -61.43€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 213 | -0.202 | -64.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 198 | -0.075 | +0.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 154 | -0.083 | -7.51€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 109 | -0.022 | +16.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 87 | -0.039 | +10.17€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 454 | -0.132 | -61.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 710 | -0.206 | -32.61€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 292 | -0.201 | -27.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 255 | -0.197 | -26.63€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 245 | -0.221 | -22.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 213 | -0.230 | -27.06€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 173 | -0.191 | +16.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 157 | -0.192 | +12.14€ | 5 | 0 |
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
| ✅ STREAK_FADE_15M | 509 | +0.032 | +16.40€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 509 | +0.032 | +16.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 241 | +0.031 | +5.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 241 | +0.031 | +5.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 35 | +0.068 | +1.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 35 | +0.068 | +1.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 54 | +0.000 | -0.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 54 | +0.000 | -0.99€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 179 | +0.036 | +11.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 179 | +0.036 | +11.12€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 2763 | -0.023 | -114.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2763 | -0.023 | -114.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 568 | -0.023 | -23.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 568 | -0.023 | -23.29€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1236 | -0.022 | -49.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1236 | -0.022 | -49.23€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 73 | -0.060 | -7.39€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 73 | -0.060 | -7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7738 | +0.023 | +117.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7738 | +0.023 | +117.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2138 | +0.021 | +22.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2138 | +0.021 | +22.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1743 | +0.035 | +51.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1743 | +0.035 | +51.78€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2342 | +0.012 | +4.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2342 | +0.012 | +4.47€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1515 | +0.030 | +39.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1515 | +0.030 | +39.06€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7266 | +0.011 | -45.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7266 | +0.011 | -45.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2920 | +0.015 | -10.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2920 | +0.015 | -10.38€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2840 | +0.012 | -18.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2840 | +0.012 | -18.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1506 | +0.004 | -16.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1506 | +0.004 | -16.99€ | 2 | 0 |
| ✅ UPDOWN_GBM | 36882 | +0.030 | +2155.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9969 | +0.067 | +1784.30€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1369 | +0.005 | +7.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 23150 | +0.018 | +341.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2251 | +0.006 | +23.66€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3783 | +0.066 | +403.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 658 | +0.148 | +258.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 32 | +0.000 | -0.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3093 | +0.049 | +145.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6812 | +0.035 | +464.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1263 | +0.083 | +283.32€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 370 | +0.019 | +7.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4116 | +0.031 | +152.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1008 | +0.004 | +20.70€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 55 | -0.097 | +0.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4319 | +0.038 | +254.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 618 | +0.139 | +217.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3673 | +0.022 | +39.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7828 | +0.016 | +269.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2561 | +0.045 | +266.96€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 358 | +0.006 | +6.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 4096 | +0.004 | -3.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 767 | +0.002 | -4.66€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 46 | -0.146 | +3.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8777 | +0.014 | +215.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2426 | +0.027 | +170.93€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 352 | -0.006 | -2.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5483 | +0.011 | +42.36€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 476 | +0.017 | +7.62€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 40 | -0.167 | -2.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5361 | +0.035 | +549.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2443 | +0.080 | +587.94€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 229 | -0.002 | -3.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2689 | -0.003 | -34.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 141 | -0.136 | +0.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 546 | +0.339 | +163.70€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 546 | +0.339 | +163.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 304 | +0.343 | +87.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 304 | +0.343 | +87.38€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 242 | +0.332 | +76.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 242 | +0.332 | +76.32€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11849 | -0.039 | +2491.89€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11849 | -0.039 | +2491.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 759 | -0.040 | +351.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 759 | -0.040 | +351.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2197 | -0.122 | +25.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2197 | -0.122 | +25.38€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 380 | +0.181 | +255.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 380 | +0.181 | +255.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1306 | +0.204 | +756.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1306 | +0.204 | +756.70€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3596 | -0.064 | +547.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3596 | -0.064 | +547.79€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3611 | -0.076 | +555.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3611 | -0.076 | +555.03€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 141 | +0.038 | +8.84€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 141 | +0.038 | +8.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 141 | +0.038 | +8.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 141 | +0.038 | +8.84€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 875 | +0.294 | +711.86€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 875 | +0.294 | +711.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 485 | +0.286 | +369.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 485 | +0.286 | +369.21€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 390 | +0.301 | +342.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 390 | +0.301 | +342.65€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 716 | -0.109 | -81.60€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 716 | -0.109 | -81.60€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 202 | -0.073 | -13.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 202 | -0.073 | -13.81€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 67 | -0.196 | -9.44€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 67 | -0.196 | -9.44€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2381 | +0.300 | +1197.95€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 820 | +0.248 | +114.01€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 892 | +0.289 | +381.24€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 669 | +0.376 | +702.69€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.018 n=477 — no justifica filtro, seguir monitorizando
  - _Datos_: n=477 IC=+0.018 PNL=+22.99€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 517 celda(s) pasan gate riguroso completo de 2233 evaluadas (n>=40) y 3216 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2425 IC=+0.027 PNL=+170.61€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=892/15 IC=+0.289 PNL=+381.24€ | BTC: n=820/15 IC=+0.248 PNL=+114.01€ | SOL: n=669/15 IC=+0.376 PNL=+702.69€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.106 n=308/60 | contraria IC=+0.143 n=303 | gap=-0.036 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=284, boost estimado=+0.001. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=765/40 IC=+0.002 PNL=-4.65€ | BTC#60min: n=1006/40 IC=+0.004 PNL=+20.73€ | SOL#60min: n=475/40 IC=+0.016 PNL=+7.07€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=332342 | tras_1loss IC=+0.077 n=258898 | tras_2loss IC=+0.047 n=109336/40 | gap=+0.003 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.08 con n=319 PNL=+206.87€
  - _Datos_: n=319 IC=+0.182 PNL=+206.87€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.224 > 0.08 con n=379 PNL=+286.63€
  - _Datos_: n=379 IC=+0.224 PNL=+286.63€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=40 PNL=+29.59€
  - _Datos_: n=40 IC=+0.238 PNL=+29.59€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.327 > 0.1 con n=1953 PNL=+1094.16€
  - _Datos_: n=1953 IC=+0.327 PNL=+1094.16€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=274 IC=+0.080 PNL=+34.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=274 IC=+0.080 PNL=+34.60€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=50 IC=+0.192 PNL=+34.21€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=50 IC=+0.192 PNL=+34.21€

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
  - _Estado_: n=1586 IC=+0.015 PNL=+13.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1586 IC=+0.015 PNL=+13.13€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=660 IC=-0.015 PNL=+10.03€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=660 IC=-0.015 PNL=+10.03€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=477 IC=+0.018 PNL=+22.99€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=477 IC=+0.018 PNL=+22.99€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.1 con n=2123 PNL=+1325.92€
  - _Datos_: n=2123 IC=+0.187 PNL=+1325.92€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1262 IC=+0.082 PNL=+282.79€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1262 IC=+0.082 PNL=+282.79€

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
  - _Estado_: n=539 IC=+0.010 PNL=+35.26€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=539 IC=+0.010 PNL=+35.26€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=50 IC=+0.058 PNL=+3.56€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=50 IC=+0.058 PNL=+3.56€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.258 n=97) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=97 IC=+0.258 PNL=+79.56€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.02 con n=637 PNL=+239.02€
  - _Datos_: n=637 IC=+0.120 PNL=+239.02€

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
  - _Estado_: n=12870 IC=+0.052 PNL=+1542.81€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=12870 IC=+0.052 PNL=+1542.81€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.160 < -0.1 con n=230 PNL=+20.16€
  - _Datos_: n=230 IC=-0.160 PNL=+20.16€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1882 IC=+0.048 PNL=+196.45€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1882 IC=+0.048 PNL=+196.45€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=77 IC=-0.120 PNL=+3.55€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=77 IC=-0.120 PNL=+3.55€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.1 con n=399 PNL=+115.66€
  - _Datos_: n=399 IC=+0.128 PNL=+115.66€

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
  - _Estado_: n=17746 IC=-0.137 PNL=+1219.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=17746 IC=-0.137 PNL=+1219.02€

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
  - _Estado_: n=1914 IC=+0.139 PNL=+1035.19€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1914 IC=+0.139 PNL=+1035.19€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3905 IC=+0.019 PNL=+117.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3905 IC=+0.019 PNL=+117.24€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=2056 PNL=+1064.56€
  - _Datos_: n=2056 IC=+0.086 PNL=+1064.56€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1729 PNL=-189.51€
  - _Datos_: n=1729 IC=-0.238 PNL=-189.51€

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
  - _Estado_: 35/40 ops en el filtro definido (IC actual=-0.041 PNL=+2.93€)
  - _Datos_: n=35 IC=-0.041 PNL=+2.93€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.091 n=984) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=984 IC=+0.091 PNL=+223.82€

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
  - _Estado_: n=8734 IC=+0.175 PNL=-1022.32€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8734 IC=+0.175 PNL=-1022.32€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
