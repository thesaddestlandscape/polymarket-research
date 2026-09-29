# Hipótesis automáticas — 2026-09-29 01:51 UTC
_Generado por shadow_postmortem.py sobre 658891 resoluciones (PNL=+77141.93€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=533)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.233 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.8032` → IC=+0.253 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8032 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.581` → IC=+0.203 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.581 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=604)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4766.038` → IC=+0.162 (n=190)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4766.038 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=533)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.140 (n=170)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=438)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=398)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.257 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.265 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.146)

- **PATRÓN** `banda_z` > `10.478` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.478 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.166 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=515)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3313.2914` → IC=+0.150 (n=304)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3313.2914 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.156 (n=158)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 94.0 (IC base=+0.060)

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
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **PATRÓN** `py_entrada` > `0.35` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.35 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1195.1095` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1195.1095 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.004)

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
- **FILTRO** `restante_s_al_confirmar` < `145.83` → IC=-0.219 (n=7552)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.83
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=22656)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.32` → IC=-0.246 (n=974)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2925)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `126.99` → IC=-0.308 (n=890)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.99
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2671)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.14` → IC=-0.204 (n=1838)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.14
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=5519)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.69` → IC=-0.337 (n=1487)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.69
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=4461)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.230 (n=357)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=411)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=540)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=564)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.207 (n=14805)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3662)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5607.146` → IC=+0.177 (n=2351)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5607.146 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=12578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=15262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11805)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=5966)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7792.686` → IC=+0.172 (n=2269)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7792.686 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=1725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `15909.0735` → IC=+0.238 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15909.0735 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=1598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `15830.8412` → IC=+0.214 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15830.8412 (IC base=+0.197)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.172 (n=343)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.62 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=383)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.100)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.141 (n=868)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.162 (n=226)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.100)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.345 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.365 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.232 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `4232.2075` → IC=+0.231 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4232.2075 (IC base=+0.228)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.134 (n=720)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.250 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=581)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1315.39` → IC=+0.146 (n=716)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1315.39 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.402 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.154 (n=1150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.28` → IC=+0.310 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.28 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=761)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.153)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `1222.0032` → IC=+0.155 (n=233)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1222.0032 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.222 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.76` → IC=-0.289 (n=131)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=12609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=12001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.228 (n=4067)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `3571.1845` → IC=+0.331 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3571.1845 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=2855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.171 (n=2859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.174 (n=2874)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.251 (n=1045)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.342 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.246)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=2812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2397)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.251 (n=2614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.323 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=2771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.195 (n=2166)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.464 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `11185.2288` → IC=+0.458 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11185.2288 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.445 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `14179.602` → IC=+0.446 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14179.602 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.449 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.462 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.425 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `3322.2122` → IC=+0.445 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.2122 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.412 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.425 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.410)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=37559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16591)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=6468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7022)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=6759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=6706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.263 (n=3831)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=6838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6818)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=6272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=2882)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=5692)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.125 (n=5291)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=5361)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=6997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.61` → IC=+0.138 (n=5285)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.61 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=2862)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.14` → IC=+0.125 (n=2635)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.14 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=2636)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.137 (n=3034)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.29` → IC=+0.141 (n=2630)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 3.29 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=2830)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.127 (n=2664)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.2 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=2970)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=2665)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1542.4309` → IC=+0.293 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1542.4309 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.348 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `4262.2927` → IC=+0.297 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4262.2927 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1729.4046` → IC=+0.312 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1729.4046 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.352 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.345)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.345)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.345)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.349 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.345)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.345)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.434 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.438 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.434 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.455 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `1978.5089` → IC=+0.464 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.5089 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.394)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.406 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.394)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.394)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.72` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=40)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.72` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=40)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4894` → IC=+0.126 (n=8891)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4894 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.9803` → IC=+0.242 (n=2966)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9803 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.258 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.971` → IC=+0.179 (n=3399)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.971 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.251 (n=2445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `0.6158` → IC=+0.254 (n=2444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6158 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.226 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.9003` → IC=+0.211 (n=4099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9003 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.5699` → IC=+0.135 (n=10782)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5699 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6051` → IC=+0.203 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6051 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.185 (n=1696)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6971 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.8683` → IC=+0.178 (n=2571)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8683 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.224 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.4504` → IC=+0.199 (n=6548)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4504 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.213 (n=6339)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 127.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.194 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.174 (n=663)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0081 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3503` → IC=+0.173 (n=1987)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3503 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.171 (n=1332)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 11.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.178` → IC=+0.268 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.178 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.207 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.168 (n=1868)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.181 (n=1997)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.254 (n=705)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.09` → IC=+0.278 (n=517)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.09 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.291 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.246 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.245 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.274 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.5359` → IC=+0.238 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5359 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1659.1648` → IC=+0.249 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1659.1648 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.228 (n=1549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3538` → IC=+0.229 (n=1549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3538 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.238 (n=1553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9838` → IC=+0.271 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9838 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.1302` → IC=+0.224 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1302 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.46` → IC=+0.265 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.46 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.223 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0807` → IC=+0.229 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0807 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.240 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7515` → IC=+0.222 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7515 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3807` → IC=+0.233 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3807 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11001.11` → IC=+0.224 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11001.11 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.164 (n=1068)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0039 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.163 (n=535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=716)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.334` → IC=+0.193 (n=1065)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.334 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6708` → IC=+0.138 (n=266)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.6708 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.152 (n=1437)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.325` → IC=+0.155 (n=253)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.325 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.341` → IC=+0.143 (n=1466)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.341 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.148 (n=1597)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2089 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8572` → IC=+0.140 (n=1064)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8572 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.178 (n=423)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4311` → IC=+0.151 (n=1486)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4311 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.146 (n=991)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14002.5438` → IC=+0.143 (n=1064)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14002.5438 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `232.0` → IC=+0.170 (n=619)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 232.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.214 (n=663)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.193 (n=1988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1779)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.254 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.192 (n=1734)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.3561` → IC=+0.205 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3561 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.7755` → IC=+0.197 (n=1697)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7755 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2359)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.221 (n=1526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6268` → IC=+0.215 (n=1734)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6268 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0636` → IC=+0.242 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0636 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.697` → IC=+0.227 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.697 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.569` → IC=+0.212 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.569 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3508` → IC=+0.260 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3508 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7523` → IC=+0.205 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7523 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `3.2696` → IC=+0.224 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2696 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1908.66` → IC=+0.217 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.66 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.212 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.158 (n=109)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2415)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.218 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1948` → IC=+0.333 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1948 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.811` → IC=+0.167 (n=785)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.811 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.333 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.335 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.354 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.331 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.330 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.1047` → IC=+0.153 (n=632)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1047 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6671` → IC=+0.212 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6671 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.159 (n=318)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6141 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1641` → IC=+0.153 (n=318)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1641 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2309` → IC=+0.206 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2309 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5277` → IC=+0.168 (n=804)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5277 (IC base=+0.021)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=365)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.200 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=324)

- **FILTRO** `ibs_20min` > `0.2456` → IC=-0.124 (n=2405)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2456
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=1186)

- **FILTRO** `sigma_ewma_delta_pct` > `8.708` → IC=-0.215 (n=380)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.708
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3211)

- **PATRÓN** `ibs_20min` > `0.7834` → IC=+0.205 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7834 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `1.7756` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.7756 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.5528` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5528 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.4536` → IC=+0.261 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4536 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.286 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.2456` → IC=+0.128 (n=1186)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.2456 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7292` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7292 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4579` → IC=+0.235 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4579 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6727` → IC=+0.277 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6727 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.285 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6579` → IC=-0.183 (n=626)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6579
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1883)

- **FILTRO** `ibs_20min` < `0.7191` → IC=-0.157 (n=1655)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7191
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=854)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.199 (n=537)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1972)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.207 (n=915)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=2800)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.315 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2822` → IC=+0.315 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2822 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.311 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.301 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4256` → IC=+0.301 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4256 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.298 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5597` → IC=+0.277 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5597 (IC base=-0.019)

- **PATRÓN** `volumen_regimen` < `0.7292` → IC=+0.254 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7292 (IC base=-0.019)

- **PATRÓN** `volumen_regimen` > `1.2494` → IC=+0.280 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2494 (IC base=-0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.0997` → IC=+0.266 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0997 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.1375` → IC=+0.263 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1375 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5236` → IC=+0.253 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5236 (IC base=-0.019)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.197 (n=3790)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0098 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4732` → IC=+0.185 (n=10156)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4732 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.018` → IC=+0.291 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.018 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.628` → IC=+0.157 (n=5268)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.628 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.179` → IC=+0.243 (n=4072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.179 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.254 (n=3640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.270 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4634` → IC=+0.241 (n=2200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4634 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6527` → IC=+0.251 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6527 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.272 (n=6129)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.168 (n=3722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5488` → IC=+0.154 (n=9816)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5488 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7104` → IC=+0.248 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7104 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2501` → IC=+0.246 (n=3198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2501 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7094` → IC=+0.247 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7094 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.2051` → IC=+0.253 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2051 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2416` → IC=+0.305 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2416 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5947` → IC=+0.268 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5947 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2837` → IC=+0.264 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2837 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.274 (n=4373)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2532` → IC=-0.156 (n=786)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2532
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2358)

- **FILTRO** `sigma_ewma_delta_pct` > `4.528` → IC=-0.166 (n=593)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.528
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1986)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.268 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.89` → IC=+0.205 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.89 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.260 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.189 (n=336)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.212 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.206 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.0916` → IC=+0.458 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0916 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4197` → IC=+0.447 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4197 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.7565` → IC=+0.448 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7565 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.487 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8652` → IC=+0.164 (n=762)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8652 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.2995` → IC=+0.179 (n=403)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2995 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6746` → IC=+0.177 (n=943)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6746 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.203 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4039` → IC=+0.174 (n=345)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4039 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.209 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 236.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.221 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.8583` → IC=+0.232 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8583 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2683` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2683 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4375` → IC=+0.217 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4375 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.240 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.219 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 456.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.290 (n=588)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.254 (n=1771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=1774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.725` → IC=+0.280 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.725 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1009` → IC=+0.263 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1009 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `3.3088` → IC=+0.270 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3088 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1911.425` → IC=+0.257 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.425 (IC base=+0.249)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.308 (n=654)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.6263` → IC=+0.287 (n=1443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6263 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.327 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.3459` → IC=+0.290 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3459 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.685` → IC=+0.289 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.685 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.754` → IC=+0.285 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.754 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.3387` → IC=+0.294 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3387 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.5845` → IC=+0.294 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5845 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.686` → IC=+0.289 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.686 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1900.976` → IC=+0.297 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1900.976 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.287 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.282)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.773` → IC=-0.185 (n=665)

  - _Acción_: SKIP cuando `ibs_20min` > 0.773
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1996)

- **PATRÓN** `ibs_20min` > `0.9107` → IC=+0.177 (n=571)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9107 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.1858` → IC=+0.230 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1858 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `0.9978` → IC=+0.247 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9978 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` > `0.5871` → IC=+0.224 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5871 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.0813` → IC=+0.264 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0813 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.266 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.7601` → IC=+0.239 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7601 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.258 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.224 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `0.6435` → IC=+0.244 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6435 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.257 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.808 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1178` → IC=+0.250 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1178 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.266 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7429` → IC=-0.192 (n=1206)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=+0.277 (n=1208)

- **FILTRO** `ibs_20min` > `0.68` → IC=-0.234 (n=608)

  - _Acción_: SKIP cuando `ibs_20min` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=1827)

- **FILTRO** `sigma_ewma_delta_pct` > `4.723` → IC=-0.190 (n=531)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.723
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=1904)

- **PATRÓN** `ibs_20min` > `0.7429` → IC=+0.277 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7429 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.8456` → IC=+0.325 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8456 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.659` → IC=+0.166 (n=381)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.659 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.309 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.298 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6396 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.297 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2691` → IC=+0.300 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2691 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4306` → IC=+0.325 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4306 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.317 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.5806` → IC=+0.127 (n=1609)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5806 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.2979` → IC=+0.232 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2979 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.259 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.224 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.231 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.241 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.249 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.019)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0169` → IC=+0.313 (n=960)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0169 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.286 (n=1511)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.7388` → IC=+0.324 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7388 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.315 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.662` → IC=+0.304 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.662 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.307 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` < `0.0784` → IC=+0.284 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0784 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.327 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.289 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2452.9003` → IC=+0.288 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2452.9003 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.318 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.309 (n=1026)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.1975` → IC=+0.285 (n=677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1975 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.292 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.283 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.2907` → IC=+0.317 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2907 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3169` → IC=+0.289 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3169 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` < `0.231` → IC=+0.280 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.231 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.082` → IC=+0.297 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.082 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.282 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.310 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.333 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `1.4255` → IC=+0.291 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4255 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1399` → IC=+0.279 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1399 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2399.3806` → IC=+0.282 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.3806 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.178 (n=2889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.203 (n=2884)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3609` → IC=+0.177 (n=7602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3609 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=9043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.5711` → IC=+0.220 (n=8639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5711 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.176` → IC=+0.193 (n=3703)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.176 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.352` → IC=+0.252 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.352 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.162 (n=5741)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2065 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.161 (n=5741)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6285 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2427` → IC=+0.194 (n=1748)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2427 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5592` → IC=+0.168 (n=3653)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5592 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6095` → IC=+0.175 (n=2767)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6095 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1944.8656` → IC=+0.170 (n=7718)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1944.8656 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.182 (n=7559)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 110.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.184 (n=5562)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0067 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0819` → IC=+0.212 (n=2781)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0819 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=3218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=3967)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4843` → IC=+0.226 (n=8335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4843 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.329` → IC=+0.195 (n=1405)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.329 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.156 (n=5998)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1776 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.213 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.561` → IC=+0.172 (n=3365)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.561 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6164` → IC=+0.172 (n=2549)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6164 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.178 (n=7301)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 110.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.219 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.188 (n=489)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.210 (n=1455)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=971)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.307 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.236 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.185 (n=1353)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.241 (n=973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.249 (n=986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1866` → IC=+0.293 (n=736)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1866 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3485` → IC=+0.259 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3485 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.325` → IC=+0.250 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.325 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.236 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.256 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.262 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1549.158` → IC=+0.249 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1549.158 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.242 (n=432)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0725` → IC=+0.194 (n=430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0725 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=1295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.3958` → IC=+0.226 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3958 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.209 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.472` → IC=+0.235 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.472 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.688` → IC=+0.173 (n=567)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.688 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0753` → IC=+0.166 (n=584)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0753 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.201 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5038` → IC=+0.182 (n=551)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5038 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.164 (n=417)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10526.5901` → IC=+0.169 (n=1288)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10526.5901 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.162 (n=536)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 239.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.164 (n=1219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0049 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.293` → IC=+0.163 (n=1385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.293 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5786` → IC=+0.188 (n=1385)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5786 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.161 (n=1379)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.205 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.157 (n=1385)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2129 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.151 (n=425)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.146 (n=1273)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.163 (n=399)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 211.0 (IC base=+0.137)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.216 (n=963)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2421` → IC=+0.219 (n=963)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2421 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.464` → IC=+0.275 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.464 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2028` → IC=+0.208 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2028 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.771` → IC=+0.218 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.771 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1702)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.236 (n=1088)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1023` → IC=+0.256 (n=412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1023 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.274 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.246 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.251 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3553` → IC=+0.250 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3553 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7601` → IC=+0.220 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7601 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.1845` → IC=+0.225 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1845 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1904.0224` → IC=+0.221 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.0224 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.214 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.178 (n=1219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0066 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.429` → IC=+0.160 (n=1384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.429 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3616` → IC=+0.196 (n=1384)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3616 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1538` → IC=+0.176 (n=906)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1538 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.226 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.855` → IC=+0.156 (n=923)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.855 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.146 (n=1384)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6206 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.196 (n=218)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.161 (n=452)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.167 (n=452)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5222.8208` → IC=+0.184 (n=923)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 5222.8208 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.148 (n=1323)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 159.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=1461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3828` → IC=+0.145 (n=1461)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3828 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6511` → IC=+0.171 (n=1461)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6511 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.961` → IC=+0.162 (n=515)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.961 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.149 (n=974)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8525 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.176 (n=217)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8112` → IC=+0.140 (n=892)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8112 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.5241` → IC=+0.125 (n=446)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.5241 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9730.5722` → IC=+0.166 (n=662)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9730.5722 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.123 (n=1273)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 155.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.151 (n=715)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=1620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.203 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.8341` → IC=+0.208 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8341 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.76` → IC=+0.249 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.76 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2002` → IC=+0.132 (n=1576)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2002 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.124 (n=1581)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.0983` → IC=+0.124 (n=599)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0983 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.134 (n=670)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1639)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2872.7619` → IC=+0.196 (n=715)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2872.7619 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.137 (n=1220)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 48.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.161 (n=708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.105` → IC=+0.167 (n=536)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.105 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.215 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2097` → IC=+0.146 (n=1483)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2097 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.622` → IC=+0.132 (n=335)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 7.622 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.151 (n=536)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6381 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.160 (n=283)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4573` → IC=+0.145 (n=486)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4573 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.137 (n=485)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2729.0252` → IC=+0.164 (n=728)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2729.0252 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.126 (n=1406)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 53.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.225 (n=1334)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.1357` → IC=+0.207 (n=499)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1357 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.259 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5119` → IC=+0.215 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5119 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.239 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2016` → IC=+0.206 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2016 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.215 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6251 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.261 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1457` → IC=+0.212 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1457 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.409` → IC=+0.209 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.409 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2434.1618` → IC=+0.204 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2434.1618 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.224 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.217 (n=702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.230 (n=516)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=716)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.0205` → IC=+0.301 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0205 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.2049` → IC=+0.225 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2049 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.392` → IC=+0.246 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.392 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6333` → IC=+0.217 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6333 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.283 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1966` → IC=+0.200 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1966 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.203 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2369.7134` → IC=+0.212 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2369.7134 (IC base=+0.207)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.169 (n=731)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0086 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3453` → IC=+0.165 (n=1925)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3453 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.5183` → IC=+0.195 (n=1954)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5183 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.8238` → IC=+0.180 (n=348)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.8238 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.726` → IC=+0.188 (n=976)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.726 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.182 (n=1302)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.871 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.162 (n=651)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.2084 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.173 (n=598)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.171 (n=706)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.5403` → IC=+0.170 (n=706)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5403 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.165 (n=2475)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2199.08` → IC=+0.163 (n=2187)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2199.08 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.177 (n=1968)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 148.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.139 (n=1503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0057 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.3457` → IC=+0.130 (n=1984)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.3457 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=2261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.0561` → IC=+0.194 (n=752)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0561 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2132` → IC=+0.122 (n=2040)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2132 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.2241` → IC=+0.122 (n=2050)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2241 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.141 (n=564)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.445` → IC=+0.151 (n=726)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.445 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2760.3927` → IC=+0.124 (n=2014)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2760.3927 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.134 (n=942)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 28.0 (IC base=+0.115)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.158 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0039 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.148 (n=549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.177 (n=515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.6559` → IC=+0.204 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6559 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.156 (n=184)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1213` → IC=+0.136 (n=446)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1213 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.153 (n=249)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6213` → IC=+0.186 (n=183)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6213 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.1564` → IC=+0.133 (n=568)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1564 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0914` → IC=+0.145 (n=195)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0914 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.211` → IC=+0.140 (n=470)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.211 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5112` → IC=+0.135 (n=477)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5112 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `10464.6185` → IC=+0.148 (n=549)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 10464.6185 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.162 (n=350)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 230.0 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.209 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.160 (n=700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.611` → IC=+0.184 (n=615)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.611 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1836` → IC=+0.152 (n=687)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1836 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.147 (n=264)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.177` → IC=+0.139 (n=635)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.177 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.143 (n=699)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2242 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.7093` → IC=+0.149 (n=624)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7093 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1046` → IC=+0.160 (n=606)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1046 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.144 (n=689)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `313.0` → IC=+0.154 (n=587)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 313.0 (IC base=+0.137)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.274 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.2084` → IC=+0.218 (n=459)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2084 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9593` → IC=+0.272 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9593 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.216 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2186` → IC=+0.209 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2186 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.949` → IC=+0.233 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.949 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.216 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.228 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.257 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4064` → IC=+0.229 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4064 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7662` → IC=+0.232 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7662 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.1001` → IC=+0.133 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1001 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0837` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.0837 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.141 (n=285)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6885 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.139 (n=153)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.094)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.149 (n=482)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0059 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.138 (n=539)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.171 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.496` → IC=+0.190 (n=288)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.496 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.158 (n=474)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0674 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.6423` → IC=+0.138 (n=539)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6423 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4788` → IC=+0.140 (n=173)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4788 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.212` → IC=+0.167 (n=235)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.212 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=563)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3090.2601` → IC=+0.198 (n=180)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3090.2601 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.121 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0098 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.4328` → IC=+0.164 (n=442)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.4328 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `1.2161` → IC=+0.123 (n=502)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2161 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.125 (n=449)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `1.8405` → IC=+0.168 (n=317)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.8405 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2911.1338` → IC=+0.152 (n=228)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2911.1338 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.146 (n=445)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 39.0 (IC base=+0.102)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.175 (n=3731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.207 (n=3722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=11687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.9974` → IC=+0.308 (n=3722)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9974 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.9322` → IC=+0.199 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9322 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.344` → IC=+0.245 (n=2799)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.344 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.8796` → IC=+0.169 (n=4986)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8796 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.198 (n=1532)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5911` → IC=+0.191 (n=3588)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5911 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `1782.52` → IC=+0.175 (n=11165)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1782.52 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.198 (n=8646)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 83.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6758)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1503` → IC=+0.191 (n=4453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1503 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=3848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=4686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.45` → IC=+0.246 (n=8910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.45 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.252` → IC=+0.162 (n=6327)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.252 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.065` → IC=+0.201 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.065 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.735` → IC=+0.184 (n=9782)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.735 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.163 (n=3042)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7048 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.241 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.8599` → IC=+0.188 (n=6240)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8599 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.199 (n=6028)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=623)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.209 (n=1247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.3577` → IC=+0.197 (n=1867)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3577 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.612` → IC=+0.346 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.612 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2273` → IC=+0.248 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2273 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8468` → IC=+0.195 (n=1180)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8468 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.262 (n=662)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1274` → IC=+0.289 (n=663)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1274 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3551` → IC=+0.283 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3551 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.507` → IC=+0.263 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.507 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.291 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.275 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1659.7886` → IC=+0.272 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1659.7886 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.205 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1131` → IC=+0.164 (n=787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1131 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3047` → IC=+0.205 (n=1787)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3047 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.185 (n=997)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.176 (n=402)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.15` → IC=+0.155 (n=1621)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.15 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.182 (n=596)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6267 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2668` → IC=+0.187 (n=260)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2668 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1149` → IC=+0.164 (n=1524)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.1149 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.158 (n=1731)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11191.459` → IC=+0.160 (n=1596)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11191.459 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `282.0` → IC=+0.173 (n=733)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 282.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3224` → IC=+0.160 (n=1538)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3224 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=695)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.2847` → IC=+0.234 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2847 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6684` → IC=+0.159 (n=244)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6684 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1328` → IC=+0.162 (n=1402)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1328 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.518` → IC=+0.168 (n=257)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.518 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.315` → IC=+0.151 (n=1399)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.315 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.194` → IC=+0.160 (n=1538)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.194 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.198 (n=408)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4038` → IC=+0.157 (n=1440)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4038 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7588` → IC=+0.160 (n=960)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7588 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.152 (n=1181)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 413.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.261 (n=608)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.301 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.1344` → IC=+0.220 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1344 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.227 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1914.6432` → IC=+0.222 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.6432 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.238 (n=1706)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6052` → IC=+0.235 (n=1706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6052 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0138` → IC=+0.302 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0138 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.774` → IC=+0.269 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.774 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.342` → IC=+0.294 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.342 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.228 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.155` → IC=+0.237 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.155 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1904.8952` → IC=+0.241 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.8952 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.232 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.192 (n=638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0035 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4338` → IC=+0.150 (n=1907)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4338 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=1995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2845` → IC=+0.185 (n=1907)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.2845 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.364` → IC=+0.158 (n=740)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.364 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.515` → IC=+0.167 (n=310)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.515 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8719` → IC=+0.159 (n=1273)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8719 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.207 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5207` → IC=+0.154 (n=814)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5207 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1501` → IC=+0.153 (n=839)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1501 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7711.5929` → IC=+0.238 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7711.5929 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.172 (n=593)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 74.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.166 (n=1034)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0052 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3555` → IC=+0.143 (n=1365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3555 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.262 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1607` → IC=+0.134 (n=1347)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1607 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.238` → IC=+0.165 (n=231)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.238 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.147 (n=683)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6971 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.2011` → IC=+0.140 (n=517)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.2011 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.228 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.4439` → IC=+0.144 (n=1477)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4439 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `9966.3147` → IC=+0.199 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9966.3147 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.136 (n=1477)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 172.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.140 (n=1268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0082 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.192 (n=1902)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4615 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.081` → IC=+0.203 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.081 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.529` → IC=+0.239 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.529 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8902` → IC=+0.141 (n=1267)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8902 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1915)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2529.0124` → IC=+0.238 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2529.0124 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.135 (n=1495)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 53.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.177 (n=611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1353` → IC=+0.159 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1353 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6389` → IC=+0.206 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6389 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2238` → IC=+0.135 (n=1510)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2238 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.449` → IC=+0.128 (n=1763)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.449 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.158 (n=805)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7144 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.172 (n=285)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.146 (n=555)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.178 (n=609)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.128 (n=1456)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 51.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.228 (n=1684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=1977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.261 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2153` → IC=+0.234 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2153 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.219` → IC=+0.267 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.219 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.0636` → IC=+0.213 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0636 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.220 (n=1885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.245 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.5476` → IC=+0.221 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5476 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1892)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2431.0035` → IC=+0.219 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2431.0035 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.221 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.018` → IC=+0.221 (n=1330)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.018 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.218 (n=1409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.4224` → IC=+0.265 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4224 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.2232` → IC=+0.209 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2232 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.212 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.260 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.236` → IC=+0.239 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.236 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.270 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.176` → IC=+0.203 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.176 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4276` → IC=+0.203 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4276 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2377.7754` → IC=+0.208 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2377.7754 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.196 (n=1710)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 37.0 (IC base=+0.207)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=3424)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.185 (n=2992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0092 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.513` → IC=+0.182 (n=3400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.513 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.178 (n=1527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.9431` → IC=+0.235 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9431 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1848` → IC=+0.181 (n=1225)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1848 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.4756` → IC=+0.169 (n=2154)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.4756 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.152` → IC=+0.197 (n=569)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.152 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.167 (n=995)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7067 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.8918` → IC=+0.175 (n=1507)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8918 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1697` → IC=+0.204 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1697 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.181 (n=1121)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.8681` → IC=+0.180 (n=2239)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8681 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=2426)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2815.8196` → IC=+0.175 (n=3038)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2815.8196 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.202 (n=860)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.170 (n=2580)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.176 (n=1160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.182 (n=1136)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.18 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.6811` → IC=+0.177 (n=472)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6811 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.184` → IC=+0.166 (n=2576)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.184 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.1021` → IC=+0.162 (n=2130)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1021 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.160 (n=2350)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.5396` → IC=+0.164 (n=1122)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5396 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.162 (n=1699)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=3424)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `12333.4089` → IC=+0.159 (n=860)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12333.4089 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.161 (n=1675)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 85.0 (IC base=+0.155)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.202 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.182 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0033 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.232 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.193 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.206 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5463 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1436` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1436 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2023` → IC=+0.184 (n=362)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2023 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.188 (n=443)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8386` → IC=+0.212 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8386 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2983` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2983 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.211 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `12545.7532` → IC=+0.221 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.7532 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.176 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.181 (n=424)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1409 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6117` → IC=+0.146 (n=436)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6117 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.162 (n=943)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8794` → IC=+0.188 (n=642)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8794 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0686` → IC=+0.166 (n=447)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0686 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.146 (n=320)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.152 (n=639)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14911.0423` → IC=+0.162 (n=436)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 14911.0423 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.144 (n=916)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 707.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.189 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.181 (n=286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.01 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.5794` → IC=+0.172 (n=630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.5794 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.237 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.227 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.3498` → IC=+0.170 (n=758)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3498 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.201 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.6739` → IC=+0.174 (n=210)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.6739 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.170 (n=561)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2425.6331` → IC=+0.194 (n=286)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2425.6331 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.333 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `2.0` → IC=+0.296 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 2.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.1988` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1988 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.257)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.182 (n=933)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0072 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3792` → IC=+0.179 (n=933)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3792 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.185 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 4.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.190 (n=707)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5305 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.8825` → IC=+0.185 (n=354)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.8825 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.3968` → IC=+0.185 (n=996)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.3968 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.221` → IC=+0.185 (n=947)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.221 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0828` → IC=+0.176 (n=933)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0828 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6387` → IC=+0.176 (n=1060)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6387 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.195 (n=319)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.180 (n=1042)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.176 (n=930)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1056)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.202 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.184 (n=868)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.7429` → IC=+0.163 (n=868)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.7429 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.0945` → IC=+0.165 (n=867)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0945 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.6022` → IC=+0.174 (n=188)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6022 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.392` → IC=+0.166 (n=786)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.392 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.195 (n=290)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6473 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.7257` → IC=+0.159 (n=775)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7257 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.176 (n=369)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.172 (n=749)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7819.0728` → IC=+0.176 (n=775)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7819.0728 (IC base=+0.157)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.160 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.011 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.374` → IC=+0.139 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.374 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.159 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 3.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.141 (n=329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.2209` → IC=+0.191 (n=218)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2209 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.026` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.026 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8829` → IC=+0.171 (n=217)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8829 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4231` → IC=+0.163 (n=315)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4231 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=384)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3007.5542` → IC=+0.156 (n=324)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3007.5542 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.156 (n=268)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 52.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.183 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0069 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.194 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 16.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.2619` → IC=+0.234 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2619 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.18` → IC=+0.165 (n=267)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 5.18 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.3617` → IC=+0.166 (n=276)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.3617 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.9454` → IC=+0.156 (n=184)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.9454 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.224 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.6095` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.6095 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `3143.016` → IC=+0.198 (n=276)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3143.016 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.194 (n=233)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 45.0 (IC base=+0.156)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.195 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=419)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.172 (n=461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0039 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.123 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.189 (n=854)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.649 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.144 (n=510)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.429` → IC=+0.193 (n=223)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.429 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `1382.9944` → IC=+0.121 (n=621)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1382.9944 (IC base=+0.083)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.125 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0045 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.304 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.135 (n=387)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.104` → IC=+0.142 (n=132)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.104 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1373` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1373 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.142 (n=283)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.437` → IC=+0.138 (n=252)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.437 (IC base=+0.030)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=291)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.030)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.145 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0058 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4638` → IC=+0.181 (n=330)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4638 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.0809` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.0809 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.134 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0043 (IC base=+0.079)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.167 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.0673` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.0673 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.186 (n=151)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `1.1209` → IC=+0.135 (n=157)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1209 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `2.0359` → IC=+0.183 (n=118)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.0359 (IC base=+0.079)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6741` → IC=-0.136 (n=141)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6741
  - _Potencial_: sin este filtro IC_bueno=+0.221 (n=288)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=135)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.143 (n=236)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.221 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.3368` → IC=+0.190 (n=127)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3368 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.292 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `1132.8739` → IC=+0.154 (n=284)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1132.8739 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1303` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1303 (IC base=+0.012)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.256` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.256 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.3281` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.3281 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.1755` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.1755 (IC base=+0.012)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.012)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.01` → IC=-0.269 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=98)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=71)

- **PATRÓN** `ibs_20min` > `0.7843` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7843 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.056)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.136 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0066 (IC base=-0.027)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=-0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.4788` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4788 (IC base=-0.027)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.297 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=151)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=173)

- **FILTRO** `dist_vwap_pct` > `0.166` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.166
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=200)

- **FILTRO** `volumen_regimen` < `0.7209` → IC=-0.342 (n=55)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7209
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=168)

- **FILTRO** `volumen_spike_ratio` > `3.0912` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.0912
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=112)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.359 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=122)

- **FILTRO** `drift_60min` |x|> `0.2208` → IC=-0.326 (n=44)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2208
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=134)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=151)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=82)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.250 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

- **FILTRO** `dist_vwap_pct` < `0.0874` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0874
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=32)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7335` → IC=-0.446 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7335
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.389 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=49)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=60)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.127 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=259)

- **FILTRO** `dist_vwap_pct` > `0.6296` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6296
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=365)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.164 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0059 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.6422` → IC=+0.149 (n=283)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6422 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.51` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.51 (IC base=+0.083)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.128 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.004 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.178 (n=259)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1644 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.0` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.0 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.181 (n=133)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.075)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=101)

- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=93)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=93)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.163 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0034 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2299` → IC=+0.150 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2299 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.160 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.101` → IC=+0.219 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.101 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.0646` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.0646 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.794` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.794 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.138` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.138 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.6881` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.6881 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.135)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0041` → IC=-0.149 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0041
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=68)

- **FILTRO** `ibs_20min` < `0.6191` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6191
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=78)

- **FILTRO** `ibs_20min` > `0.156` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.156
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=85)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.014)

- **PATRÓN** `ibs_20min` > `0.8766` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8766 (IC base=+0.014)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.014)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.130 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0053 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `0.9491` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 0.9491 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.069)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0772` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0772
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=21)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.250 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.221 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.7027` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7027 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.225 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.046)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.2733` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2733 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.346 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.222)

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.222)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.328 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.222)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.2733` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2733 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.346 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.222)

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.222)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.328 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.222)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=801)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2902.7974` → IC=+0.159 (n=274)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2902.7974 (IC base=+0.104)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=801)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2902.7974` → IC=+0.159 (n=274)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2902.7974 (IC base=+0.104)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.199 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=85)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=140)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=222)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=208)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=44)

- **FILTRO** `libro_liquidez` < `10452.0502` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 10452.0502
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=90)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2002)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=50)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=82)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=88)

- **PATRÓN** `libro_liquidez` > `2381.729` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2381.729 (IC base=+0.035)

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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `liq_n` > 18.0 (IC base=+0.009)

- **PATRÓN** `liq_usd_total` > `62935.21` → IC=+0.152 (n=110)

  - _Acción_: Kelly boost +0.76€ cuando `liq_usd_total` > 62935.21 (IC base=+0.009)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=147)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=867)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=821)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=463)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=207)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.016)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=678)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=678)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=412)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=412)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=181)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=181)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.138 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=99)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=123)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=225)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=102)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=105)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=257)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=257)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.157 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=219)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=147)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.145 (n=390)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=994)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.138 (n=45)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=119)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=+0.012)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.149 (n=92)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.56 (IC base=+0.060)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **FILTRO** `restante_min` > `13.33` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `restante_min` > 13.33
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=63)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.250 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=64)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.146 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 9.0 (IC base=+0.086)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.131 (n=82)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=31)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=76)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=103)

- **FILTRO** `profundidad_ratio` < `19.0` → IC=-0.151 (n=41)

  - _Acción_: SKIP cuando `profundidad_ratio` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=85)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.46 (IC base=-0.016)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=122)

- **FILTRO** `restante_min` < `3.46` → IC=-0.269 (n=50)

  - _Acción_: SKIP cuando `restante_min` < 3.46
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=102)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.214 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=105)

- **FILTRO** `lag_apertura_s` > `91.82` → IC=-0.274 (n=51)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.82
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=101)

- **FILTRO** `profundidad_ratio` < `76.0` → IC=-0.218 (n=76)

  - _Acción_: SKIP cuando `profundidad_ratio` < 76.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=76)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.44 (IC base=+0.065)

- **PATRÓN** `profundidad_ratio` > `24.5` → IC=+0.140 (n=87)

  - _Acción_: Kelly boost +0.70€ cuando `profundidad_ratio` > 24.5 (IC base=+0.065)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `restante_min` < `3.76` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `restante_min` < 3.76
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=66)

- **FILTRO** `lag_apertura_s` > `74.64` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `lag_apertura_s` > 74.64
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=66)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.46 (IC base=+0.038)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.139 (n=106)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=58)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.5 (IC base=-0.030)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.259 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=139)

- **FILTRO** `restante_min` < `3.26` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `restante_min` < 3.26
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=131)

- **FILTRO** `lag_apertura_s` > `103.0` → IC=-0.147 (n=66)

  - _Acción_: SKIP cuando `lag_apertura_s` > 103.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=129)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.167 (n=3890)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=11933)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.161 (n=4013)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12404)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.202 (n=675)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=2094)

- **PATRÓN** `libro_liquidez` > `1553.6248` → IC=+0.134 (n=997)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1553.6248 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.186 (n=692)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2127)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=702)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2254)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.171 (n=678)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2086)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.171 (n=727)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=2228)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2223)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2329)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3069)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=410)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=401)

- **FILTRO** `libro_liquidez` < `17011.7455` → IC=-0.143 (n=228)

  - _Acción_: SKIP cuando `libro_liquidez` < 17011.7455
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=686)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ballena_activa_n` > `89.0` → IC=-0.218 (n=115)

  - _Acción_: SKIP cuando `ballena_activa_n` > 89.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=225)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `drift_20min_pct` |x|> `0.2312` → IC=-0.120 (n=322)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2312
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=627)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=230)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=11051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=24903)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=8925)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=27029)

- **FILTRO** `ibs_7min` < `0.2727` → IC=-0.236 (n=8983)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=26971)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12008)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=23946)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.231 (n=11104)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=34355)

- **FILTRO** `ibs_7min` > `0.2908` → IC=-0.177 (n=11363)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2908
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=34096)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=1805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4220)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=1436)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4589)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.255 (n=1987)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=4038)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.177 (n=1461)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4564)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.262 (n=1936)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=5883)

- **FILTRO** `ibs_7min` > `0.7869` → IC=-0.206 (n=1953)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7869
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5866)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.143 (n=1450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=4727)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1505)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4672)

- **FILTRO** `ibs_7min` < `0.7461` → IC=-0.199 (n=1544)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7461
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4633)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.179 (n=1539)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4638)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1450)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4844)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.183 (n=1571)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4723)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=1561)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4733)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.168 (n=1400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4325)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=1426)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4299)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.244 (n=1883)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3842)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.210 (n=1404)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4321)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=1931)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=6451)

- **FILTRO** `ibs_7min` > `0.7442` → IC=-0.174 (n=2094)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7442
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6288)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=1898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4019)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.235 (n=1742)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=4175)

- **FILTRO** `ibs_7min` < `0.74` → IC=-0.183 (n=1479)

  - _Acción_: SKIP cuando `ibs_7min` < 0.74
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4438)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.174 (n=1438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=4479)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.255 (n=1515)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4570)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.176 (n=1521)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4564)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.181 (n=1498)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4587)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1459)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4723)

- **FILTRO** `ibs_7min` < `0.2778` → IC=-0.234 (n=1545)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4637)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.168 (n=2155)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=6517)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1459)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4469)

- **FILTRO** `ibs_7min` < `0.2895` → IC=-0.225 (n=1482)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2895
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4446)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1406)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4522)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.206 (n=1917)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6290)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1147)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=571)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=332)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=575)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.134 (n=814)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.146 (n=272)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 469.512 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.199 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.134 (n=162)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 422.506 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2534.4132` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2534.4132 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 14.0 (IC base=+0.132)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 11.0 (IC base=+0.107)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.178 (n=113)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.125 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.101)

- **PATRÓN** `total_vol_5m` < `390.044` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.044 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 75.0 (IC base=+0.101)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.178 (n=141)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.240 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `6163.256` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 6163.256 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3246.8834` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3246.8834 (IC base=+0.135)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.151 (n=147)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.131 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3582.6278` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3582.6278 (IC base=+0.104)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.291 (n=213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=214)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.256 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=44)

- **FILTRO** `T_h` > `95.4629` → IC=-0.412 (n=32)

  - _Acción_: SKIP cuando `T_h` > 95.4629
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.112)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=60)

- **FILTRO** `T_h` < `39.9918` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `T_h` < 39.9918
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=60)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.172 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=106)

- **FILTRO** `T_h` > `70.6078` → IC=-0.128 (n=315)

  - _Acción_: SKIP cuando `T_h` > 70.6078
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=106)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.324 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=271)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.326 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=270)

- **FILTRO** `T_h` > `61.7816` → IC=-0.316 (n=269)

  - _Acción_: SKIP cuando `T_h` > 61.7816
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=91)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `63.9952` → IC=-0.143 (n=110)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `pct_vs_K` |x|> `2.84` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.84
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=112)

- **FILTRO** `T_h` > `144.522` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `T_h` > 144.522
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=104)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.438 (n=46)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=90)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9836` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `T_h` > 135.9836
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.400 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=90)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.333 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=85)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=85)

- **FILTRO** `T_h` > `60.9515` → IC=-0.331 (n=75)

  - _Acción_: SKIP cuando `T_h` > 60.9515
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=38)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0073` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=78)

- **FILTRO** `T_h` > `135.7816` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `T_h` > 135.7816
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=78)

- **FILTRO** `pct_vs_K` |x|> `3.8` → IC=-0.230 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

- **FILTRO** `sigma_h` < `0.0146` → IC=-0.375 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0146
  - _Potencial_: sin este filtro IC_bueno=-0.315 (n=25)

- **FILTRO** `T_h` > `58.2361` → IC=-0.373 (n=53)

  - _Acción_: SKIP cuando `T_h` > 58.2361
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0286` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.0286 (IC base=-0.043)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.370)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.405 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.370)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.405 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.370)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.370)

- **PATRÓN** `dist_50` > `0.4222` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4222 (IC base=+0.370)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.412 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.370)

- **PATRÓN** `edge` > `0.096` → IC=+0.450 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.415)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.415)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.444 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.415)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.415)

- **PATRÓN** `T_h` > `1.3581` → IC=+0.446 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.3581 (IC base=+0.415)

- **PATRÓN** `dist_50` > `0.4085` → IC=+0.481 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4085 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.473 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.415)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1078` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1078 (IC base=+0.414)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.400 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.414)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.414)

- **PATRÓN** `T_h` < `0.9168` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9168 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.4178` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4178 (IC base=+0.414)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.447)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.473 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.447)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.447)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.447)

- **PATRÓN** `dist_50` > `0.4692` → IC=+0.466 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4692 (IC base=+0.447)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.447)

- **PATRÓN** `edge` > `0.1155` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.486 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.462)

- **PATRÓN** `T_h` > `0.8977` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8977 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.5` → IC=+0.484 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=208)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=312)

- **FILTRO** `streak_estiramiento` > `0.8486` → IC=-0.167 (n=67)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8486
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=204)

- **PATRÓN** `streak_estiramiento` < `0.3906` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `streak_estiramiento` < 0.3906 (IC base=+0.033)

- **PATRÓN** `streak_estiramiento` < `0.5687` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `streak_estiramiento` < 0.5687 (IC base=+0.028)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=20)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=-0.013)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `2331737.7` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 2331737.7
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=48)

- **FILTRO** `streak_estiramiento` > `0.4576` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4576
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=38)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.4576 (IC base=-0.008)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 49.0 (IC base=+0.053)

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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=441)

### STREAK_FADE_60M
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
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=672)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1244)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=823)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=803)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3108)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1567)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1575)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.193 (n=603)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0043 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.227 (n=603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.198 (n=797)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.187)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2172` → IC=+0.193 (n=603)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2172 (IC base=+0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.234 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=1699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.189 (n=1878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_15` > `0.6077` → IC=+0.267 (n=1808)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6077 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.1199` → IC=+0.185 (n=909)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1199 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.822` → IC=+0.273 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.822 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `8758.263` → IC=+0.198 (n=603)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 8758.263 (IC base=+0.187)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=752)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.220 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.279 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.209)

- **PATRÓN** `drift_15min` |x|≤ `0.3839` → IC=+0.213 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3839 (IC base=+0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2587` → IC=+0.250 (n=134)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2587 (IC base=+0.209)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4004` → IC=+0.243 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4004 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.243 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.209)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.274 (n=401)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.269 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.209 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.385` → IC=+0.274 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.385 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `16049.3542` → IC=+0.235 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.3542 (IC base=+0.209)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.723` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.723
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=459)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5778` → IC=-0.153 (n=142)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5778
  - _Potencial_: sin este filtro IC_bueno=+0.223 (n=428)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.176 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0035 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.134 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.005 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.154 (n=189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.129)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.176 (n=143)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.129)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.167 (n=157)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.138 (n=448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_15` > `0.5778` → IC=+0.223 (n=428)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5778 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.144 (n=338)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.389` → IC=+0.221 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.389 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `9036.5854` → IC=+0.143 (n=194)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 9036.5854 (IC base=+0.129)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=123)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.284 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.196 (n=189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0757` → IC=+0.186 (n=192)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.0757 (IC base=+0.174)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.220 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.192 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.256 (n=215)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5926 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.178 (n=209)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.286` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.286 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `3066.3233` → IC=+0.260 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3066.3233 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.206 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.174)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6927` → IC=-0.150 (n=101)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6927
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1147)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.006)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.271 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.225 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0976` → IC=+0.202 (n=310)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0976 (IC base=+0.196)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `ibs_15` > `0.5695` → IC=+0.286 (n=465)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5695 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.3546` → IC=+0.209 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3546 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.5516` → IC=+0.196 (n=505)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.5516 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.251` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.251 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.374` → IC=+0.199 (n=423)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 7.374 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2911.0954` → IC=+0.283 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.0954 (IC base=+0.196)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.150 (n=524)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1176 (IC base=+0.053)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.358 (n=300)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.350)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.375 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.350)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.351 (n=301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.350)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.362 (n=448)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=+0.350)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.389 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.350)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.350)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.389 (n=449)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.350)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.391 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.018` → IC=+0.352 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.018 (IC base=+0.350)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.353 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.366 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.350)

- **PATRÓN** `ballena_activa_n` < `457.0` → IC=+0.370 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 457.0 (IC base=+0.350)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.364 (n=218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.355)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.371 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.355)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.371 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.355)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.365 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.355)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1524` → IC=+0.374 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1524 (IC base=+0.355)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.355)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.355)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.388 (n=248)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.355)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.407 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.355)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.355)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.359 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.355)

- **PATRÓN** `libro_liquidez` > `11121.9309` → IC=+0.374 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11121.9309 (IC base=+0.355)

- **PATRÓN** `ballena_activa_n` < `569.0` → IC=+0.401 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 569.0 (IC base=+0.355)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.383 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.341)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.347 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.341)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.363 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.341)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.370 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.407 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.341)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.392 (n=201)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` < `0.1197` → IC=+0.344 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1197 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.352 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.347 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `3456.6166` → IC=+0.353 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3456.6166 (IC base=+0.341)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.348 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.341)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.224 (n=714)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2144)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.205 (n=988)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1870)

- **FILTRO** `libro_liquidez` < `3080.6998` → IC=-0.146 (n=1429)

  - _Acción_: SKIP cuando `libro_liquidez` < 3080.6998
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1429)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.248 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6389` → IC=+0.269 (n=686)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6389 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2727` → IC=+0.188 (n=553)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2727 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1212` → IC=+0.249 (n=1355)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1212 (IC base=-0.027)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.243 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.027)

- **PATRÓN** `ibs_15` < `0.3519` → IC=+0.273 (n=2032)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3519 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` > `0.6856` → IC=+0.295 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6856 (IC base=-0.027)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.214 (n=435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=1307)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.228 (n=435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1307)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.253 (n=310)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1432)

- **FILTRO** `libro_liquidez` < `16338.0038` → IC=-0.204 (n=1149)

  - _Acción_: SKIP cuando `libro_liquidez` < 16338.0038
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=593)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.151 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0028 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.272 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.120 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.329 (n=197)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.281 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.081)

- **PATRÓN** `ibs_15` < `0.213` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.213 (IC base=-0.199)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=418)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0068 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.163 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0041 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.212 (n=144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.143)

- **PATRÓN** `drift_15min` |x|≤ `0.4178` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `drift_15min` |x|≤ 0.4178 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.143 (n=292)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.6625` → IC=+0.254 (n=327)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6625 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1102` → IC=+0.175 (n=232)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1102 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.024` → IC=+0.143 (n=281)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 9.024 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=418)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `10970.2258` → IC=+0.180 (n=148)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 10970.2258 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.251 (n=793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4422` → IC=+0.238 (n=793)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4422 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.4747` → IC=+0.258 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4747 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2075` → IC=+0.260 (n=360)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2075 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.250 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.2756` → IC=+0.280 (n=697)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2756 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.7529` → IC=+0.314 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7529 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.868` → IC=+0.257 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.868 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.366` → IC=+0.240 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.366 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.227 (n=338)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=339)

- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.223 (n=229)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=448)

- **FILTRO** `drift_15min` |x|> `0.8935` → IC=-0.272 (n=169)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8935
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=508)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.192 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.5625 (IC base=-0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0777` → IC=+0.229 (n=312)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0777 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.259 (n=350)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7501` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7501 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.222 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.259 (n=409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=411)

- **FILTRO** `sigma_ewma_delta_pct` > `7.05` → IC=-0.207 (n=254)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.05
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=566)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=215)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=605)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1379` → IC=+0.300 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1379 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1078` → IC=+0.334 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1078 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3391` → IC=+0.305 (n=525)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3391 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8999` → IC=+0.340 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8999 (IC base=-0.039)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.048)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.048)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.303 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0563` → IC=+0.325 (n=243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0563 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2411` → IC=+0.307 (n=242)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2411 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.223` → IC=+0.322 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.223 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8408` → IC=+0.328 (n=726)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8408 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.336 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.349 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12836.5354` → IC=+0.298 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12836.5354 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.293 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.286 (n=354)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.337 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.262` → IC=+0.306 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.262 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.311 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.317 (n=396)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4113` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4113 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.367 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.328 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.312 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.303 (n=221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.298 (n=221)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.328 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8539` → IC=+0.340 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8539 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.308 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.293 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.331 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.296 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=219)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1149` → IC=-0.162 (n=72)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1149
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=219)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.164 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=336)

- **FILTRO** `ballena_activa_n` > `56.0` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ballena_activa_n` > 56.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=140)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0702` → IC=-0.127 (n=57)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0702
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=116)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=130)

- **FILTRO** `drift_60min` |x|> `0.1544` → IC=-0.208 (n=22)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

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

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.2131` → IC=-0.231 (n=24)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2131
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

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
- **PATRÓN** `T_h` > `79.3918` → IC=+0.218 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.203)

- **PATRÓN** `ratio` < `0.9775` → IC=+0.468 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.203)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0094` → IC=+0.291 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0094 (IC base=+0.331)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.4188` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.4188 (IC base=+0.183)

- **PATRÓN** `ratio` < `0.973` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.183)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.292 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.282)

- **PATRÓN** `ratio` > `1.0467` → IC=+0.367 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0467 (IC base=+0.282)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `81.6124` → IC=+0.266 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6124 (IC base=+0.240)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.420 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.240)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.327 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.311)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.330 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.311)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1332` → IC=+0.459 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6077 sube el IC de +0.187 a +0.267 en UPDOWN_GBM#15min (n=1808). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.209 a +0.274 en UPDOWN_GBM#BTC#15min (n=401). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5778 sube el IC de +0.129 a +0.223 en UPDOWN_GBM#ETH#15min (n=428). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.174 a +0.256 en UPDOWN_GBM#SOL#15min (n=215). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.196 a +0.286 en UPDOWN_GBM#XRP#15min (n=465). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.053 a +0.150 en UPDOWN_GBM#XRP#15min (n=524). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6389 sube el IC de -0.068 a +0.269 en UPDOWN_GBM_15M_TARDIO (n=686). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3519 sube el IC de -0.027 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=2032). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.081 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=197). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.213 sube el IC de -0.199 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6625 sube el IC de +0.143 a +0.254 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2756 sube el IC de +0.234 a +0.280 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=697). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.174 a +0.192 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=50). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.259 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=350). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8408 sube el IC de +0.291 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=726). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.287 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=396). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8539 sube el IC de +0.294 a +0.340 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.350 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=449). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.355 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=248). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.341 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=201). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1402 | +0.100 | +200.21€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1402 | +0.100 | +200.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 29 | +0.016 | -3.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 29 | +0.016 | -3.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1058 | +0.109 | +174.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1058 | +0.109 | +174.14€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 30208 | -0.084 | -4032.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1586 | -0.026 | -212.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28622 | -0.087 | -3820.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3899 | -0.097 | -651.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3899 | -0.097 | -651.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1586 | -0.026 | -212.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1586 | -0.026 | -212.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3561 | -0.099 | -810.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3561 | -0.099 | -810.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7857 | -0.015 | -752.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7857 | -0.015 | -752.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7357 | -0.090 | -470.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7357 | -0.090 | -470.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5948 | -0.165 | -1134.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5948 | -0.165 | -1134.69€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 20996 | -0.025 | +3848.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5438 | +0.001 | +1787.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 15558 | -0.033 | +2060.18€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 20996 | -0.025 | +3848.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5438 | +0.001 | +1787.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 15558 | -0.033 | +2060.18€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1482 | -0.103 | -192.14€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 172 | -0.052 | -21.52€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 784 | -0.090 | -97.80€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 148 | -0.047 | -16.30€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 101521 | +0.113 | -4960.13€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14906 | +0.184 | -458.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 417 | -0.068 | -54.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 79725 | +0.101 | -4215.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6473 | +0.107 | -232.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13252 | +0.100 | -1048.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 48 | -0.160 | +1.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13189 | +0.101 | -1038.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20414 | +0.131 | -367.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4648 | +0.202 | -128.35€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13221 | +0.113 | -180.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2503 | +0.099 | -35.82€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13291 | +0.090 | -1191.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 55 | -0.114 | -9.21€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13221 | +0.091 | -1170.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21561 | +0.124 | -414.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5839 | +0.176 | -83.02€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13365 | +0.105 | -260.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2345 | +0.100 | -61.70€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19740 | +0.114 | -1153.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4267 | +0.187 | -249.02€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 320 | -0.028 | -0.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13528 | +0.092 | -769.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1625 | +0.129 | -134.49€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13263 | +0.100 | -785.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 49 | -0.029 | +9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13201 | +0.100 | -795.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16122 | +0.193 | -1025.74€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16122 | +0.193 | -1025.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3807 | +0.167 | -400.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3807 | +0.167 | -400.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1504 | +0.206 | -1.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1504 | +0.206 | -1.42€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3746 | +0.181 | -309.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3746 | +0.181 | -309.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3304 | +0.241 | -102.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3304 | +0.241 | -102.75€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3682 | +0.191 | -225.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3682 | +0.191 | -225.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 758 | +0.429 | -22.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 758 | +0.429 | -22.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 294 | +0.439 | -2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 294 | +0.439 | -2.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 288 | +0.428 | -8.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 288 | +0.428 | -8.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 164 | +0.410 | -9.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 164 | +0.410 | -9.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 55753 | +0.197 | -4351.91€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 55753 | +0.197 | -4351.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9609 | +0.178 | -1090.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9609 | +0.178 | -1090.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8927 | +0.222 | -335.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8927 | +0.222 | -335.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9626 | +0.174 | -1124.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9626 | +0.174 | -1124.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9018 | +0.217 | -375.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9018 | +0.217 | -375.36€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9222 | +0.203 | -610.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9222 | +0.203 | -610.85€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9351 | +0.193 | -813.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9351 | +0.193 | -813.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 21135 | +0.117 | +172.58€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 21135 | +0.117 | +172.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10495 | +0.120 | +132.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10495 | +0.120 | +132.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10640 | +0.114 | +39.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10640 | +0.114 | +39.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1579 | +0.287 | -27.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1579 | +0.287 | -27.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 704 | +0.278 | -19.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 704 | +0.278 | -19.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 761 | +0.286 | -11.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 761 | +0.286 | -11.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 114 | +0.345 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 114 | +0.345 | +3.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 701 | +0.435 | -5.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 701 | +0.435 | -5.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 335 | +0.432 | -5.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 335 | +0.432 | -5.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 321 | +0.438 | -0.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 321 | +0.438 | -0.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1206 | +0.067 | -62.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 427 | +0.050 | -40.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 779 | +0.076 | -21.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 949 | +0.074 | -30.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 170 | +0.064 | -9.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 779 | +0.076 | -21.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 193 | +0.013 | -35.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 193 | +0.013 | -35.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 39744 | +0.098 | -1149.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3259 | +0.088 | +18.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 36485 | +0.099 | -1167.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 22197 | +0.102 | -335.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3259 | +0.088 | +18.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 18938 | +0.104 | -354.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7642 | +0.110 | -6.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7642 | +0.110 | -6.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9905 | +0.080 | -806.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9905 | +0.080 | -806.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 849 | +0.214 | -101.09€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 849 | +0.214 | -101.09€ | 1 | 4 |
| ✅ GBM_LATE_15M | 28188 | +0.085 | +13746.08€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 28188 | +0.085 | +13746.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4715 | +0.197 | +3505.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4715 | +0.197 | +3505.96€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 4193 | +0.179 | +3001.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4193 | +0.179 | +3001.42€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 4960 | +0.198 | +3700.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4960 | +0.198 | +3700.55€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4073 | +0.026 | +960.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4073 | +0.026 | +960.53€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4023 | -0.032 | +932.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4023 | -0.032 | +932.53€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6224 | -0.039 | +1645.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6224 | -0.039 | +1645.09€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 30026 | +0.086 | +15883.15€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 30026 | +0.086 | +15883.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5723 | +0.012 | +3012.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5723 | +0.012 | +3012.03€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6268 | +0.015 | +1336.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6268 | +0.015 | +1336.90€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4272 | +0.264 | +4337.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4272 | +0.264 | +4337.96€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4945 | +0.005 | +987.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4945 | +0.005 | +987.46€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4849 | +0.031 | +1914.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4849 | +0.031 | +1914.87€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3969 | +0.280 | +4293.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3969 | +0.280 | +4293.93€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 22631 | +0.170 | +17223.32€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 22631 | +0.170 | +17223.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3409 | +0.209 | +2748.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3409 | +0.209 | +2748.11€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3563 | +0.150 | +2640.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3563 | +0.150 | +2640.16€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3572 | +0.210 | +2864.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3572 | +0.210 | +2864.72€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3792 | +0.134 | +2700.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3792 | +0.134 | +2700.37€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4242 | +0.119 | +3042.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4242 | +0.119 | +3042.04€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4053 | +0.205 | +3227.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4053 | +0.205 | +3227.92€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5921 | +0.137 | +2721.48€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5921 | +0.137 | +2721.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1662 | +0.135 | +831.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1662 | +0.135 | +831.80€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1780 | +0.153 | +860.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1780 | +0.153 | +860.34€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1387 | +0.119 | +549.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1387 | +0.119 | +549.99€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 28378 | +0.177 | +21545.44€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 28378 | +0.177 | +21545.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4494 | +0.224 | +3853.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4494 | +0.224 | +3853.36€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4432 | +0.151 | +2976.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4432 | +0.151 | +2976.58€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4701 | +0.226 | +4048.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4701 | +0.226 | +4048.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4609 | +0.135 | +3191.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4609 | +0.135 | +3191.73€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4969 | +0.117 | +3321.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4969 | +0.117 | +3321.23€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5173 | +0.209 | +4154.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5173 | +0.209 | +4154.39€ | 0 | 25 |
| ✅ GBM_LATE_5M | 7972 | +0.165 | +5069.39€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 7972 | +0.165 | +5069.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1840 | +0.153 | +1253.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1840 | +0.153 | +1253.51€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 907 | +0.172 | +579.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 907 | +0.172 | +579.71€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2569 | +0.167 | +1600.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2569 | +0.167 | +1600.53€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 799 | +0.147 | +424.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 799 | +0.147 | +424.59€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1954 | +0.068 | +748.57€ | 1 | 15 |
| ✅ GBM_LATE_60M#60min | 1954 | +0.068 | +748.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 720 | +0.091 | +270.70€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 720 | +0.091 | +270.70€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 640 | +0.072 | +302.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 640 | +0.072 | +302.88€ | 2 | 14 |
| ✅ GBM_LATE_60M#SOL | 594 | +0.035 | +174.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 594 | +0.035 | +174.99€ | 2 | 8 |
| 🚫 GBM_LATE_60M_FADE | 407 | -0.258 | -24.31€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 407 | -0.258 | -24.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 153 | -0.223 | -7.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 153 | -0.223 | -7.57€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 135 | -0.259 | -8.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 135 | -0.259 | -8.36€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 119 | -0.293 | -8.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 119 | -0.293 | -8.38€ | 2 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 768 | +0.079 | +178.60€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 768 | +0.079 | +178.60€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 302 | +0.069 | +62.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 302 | +0.069 | +62.47€ | 3 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 231 | +0.045 | +17.21€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 231 | +0.045 | +17.21€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 235 | +0.124 | +98.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 235 | +0.124 | +98.92€ | 1 | 11 |
| ✅ LATE_WINDOW_5MIN | 107 | +0.262 | +91.86€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 107 | +0.262 | +91.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 107 | +0.262 | +91.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 107 | +0.262 | +91.86€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2234 | +0.103 | +601.96€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2234 | +0.103 | +601.96€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2234 | +0.103 | +601.96€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2234 | +0.103 | +601.96€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 399 | -0.074 | -32.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 399 | -0.074 | -32.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 103 | -0.043 | -3.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 103 | -0.043 | -3.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 147 | -0.024 | -4.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 147 | -0.024 | -4.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2201 | +0.007 | +17.59€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2201 | +0.007 | +17.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 118 | +0.017 | -2.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 118 | +0.017 | -2.96€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 255 | -0.018 | +8.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 255 | -0.018 | +8.25€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 175 | -0.025 | -5.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 175 | -0.025 | -5.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 914 | +0.021 | +20.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 914 | +0.021 | +20.06€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 503 | +0.003 | -3.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 503 | +0.003 | -3.64€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 236 | +0.004 | +1.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 236 | +0.004 | +1.75€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1185 | -0.041 | -23.90€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1185 | -0.041 | -23.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 334 | -0.042 | -13.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 334 | -0.042 | -13.08€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 402 | -0.025 | +0.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 402 | -0.025 | +0.06€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 449 | -0.054 | -10.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 449 | -0.054 | -10.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2630 | -0.014 | +68.63€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1246 | -0.017 | +28.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1384 | -0.012 | +40.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 81 | +0.018 | +7.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 43 | +0.056 | +8.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 38 | -0.025 | -0.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 614 | +0.002 | +34.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 283 | -0.002 | +11.07€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 331 | +0.004 | +22.93€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 329 | -0.020 | +8.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 159 | -0.053 | -6.98€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 170 | +0.012 | +15.41€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 520 | -0.031 | -14.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 239 | -0.027 | -5.24€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 281 | -0.034 | -9.04€ | 5 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 489 | -0.009 | +23.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 241 | -0.014 | +13.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 248 | -0.004 | +10.36€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 597 | -0.022 | +9.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 281 | -0.016 | +7.77€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 316 | -0.028 | +1.79€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 32240 | -0.006 | +1455.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 32240 | -0.006 | +1455.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5701 | +0.020 | +716.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5701 | +0.020 | +716.42€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4920 | -0.030 | -71.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4920 | -0.030 | -71.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5775 | +0.016 | +514.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5775 | +0.016 | +514.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4706 | -0.053 | -155.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4706 | -0.053 | -155.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5419 | -0.009 | +208.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5419 | -0.009 | +208.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5719 | +0.010 | +243.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5719 | +0.010 | +243.28€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6010 | -0.060 | -150.84€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6010 | -0.060 | -150.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1447 | -0.085 | -41.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1447 | -0.085 | -41.63€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 682 | -0.124 | -31.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 682 | -0.124 | -31.24€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1766 | -0.078 | -33.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1766 | -0.078 | -33.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3346 | +0.004 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3346 | +0.004 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1316 | +0.007 | +7.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1316 | +0.007 | +7.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 81413 | -0.072 | +1770.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 81413 | -0.072 | +1770.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13844 | -0.076 | +823.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13844 | -0.076 | +823.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12471 | -0.095 | -634.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12471 | -0.095 | -634.99€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 14107 | -0.067 | +747.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 14107 | -0.067 | +747.54€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12002 | -0.093 | -206.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12002 | -0.093 | -206.31€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14854 | -0.048 | +390.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14854 | -0.048 | +390.80€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14135 | -0.062 | +649.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14135 | -0.062 | +649.44€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7802 | -0.028 | -140.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7802 | -0.028 | -140.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1779 | -0.036 | -15.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1779 | -0.036 | -15.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2206 | -0.023 | -29.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2206 | -0.023 | -29.34€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1064 | -0.045 | -20.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1064 | -0.045 | -20.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 754 | -0.021 | -24.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 754 | -0.021 | -24.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1221 | +0.110 | +422.42€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1085 | +0.116 | +409.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 245 | +0.132 | +116.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 245 | +0.132 | +116.50€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 209 | +0.107 | +58.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 209 | +0.107 | +58.12€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 226 | +0.101 | +79.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 226 | +0.101 | +79.96€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 187 | +0.135 | +88.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 187 | +0.135 | +88.49€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 218 | +0.104 | +66.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 218 | +0.104 | +66.76€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 625 | -0.044 | -51.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 625 | -0.044 | -51.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 126 | -0.008 | +2.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 126 | -0.008 | +2.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 83 | -0.076 | -13.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 83 | -0.076 | -13.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 183 | -0.062 | -24.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 183 | -0.062 | -24.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 127 | -0.019 | -3.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 127 | -0.019 | -3.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 106 | -0.056 | -11.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 106 | -0.056 | -11.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 621 | -0.110 | -54.39€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 284 | -0.161 | -66.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 231 | -0.200 | -67.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 53 | +0.009 | +0.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 216 | -0.073 | -0.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 166 | -0.077 | -6.90€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 50 | -0.058 | +6.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 121 | -0.053 | +12.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 97 | -0.076 | +6.36€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 24 | +0.038 | +6.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 494 | -0.135 | -67.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 127 | -0.012 | +13.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 781 | -0.200 | -33.26€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 325 | -0.197 | -28.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 284 | -0.196 | -28.79€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 41 | -0.198 | +0.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 266 | -0.216 | -24.23€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 231 | -0.225 | -29.32€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 35 | -0.149 | +5.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 190 | -0.177 | +19.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 174 | -0.176 | +14.88€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 689 | -0.202 | -43.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 92 | -0.181 | +9.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 324 | +0.405 | +239.02€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 33 | +0.071 | -3.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 33 | +0.071 | -3.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 81 | +0.380 | +59.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 81 | +0.380 | +59.35€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 210 | +0.462 | +183.10€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 210 | +0.462 | +183.10€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 324 | +0.405 | +239.02€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 558 | +0.030 | +15.23€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 558 | +0.030 | +15.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 270 | +0.029 | +3.56€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 270 | +0.029 | +3.56€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 58 | -0.017 | -2.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 58 | -0.017 | -2.10€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 193 | +0.033 | +10.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 193 | +0.033 | +10.59€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2903 | -0.021 | -113.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2903 | -0.021 | -113.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 877 | -0.019 | -29.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 877 | -0.019 | -29.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 572 | -0.023 | -23.22€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 572 | -0.023 | -23.22€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1298 | -0.018 | -47.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1298 | -0.018 | -47.32€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 77 | -0.044 | -5.84€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 77 | -0.044 | -5.84€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8562 | +0.023 | +130.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8562 | +0.023 | +130.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2349 | +0.025 | +32.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2349 | +0.025 | +32.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1933 | +0.033 | +53.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1933 | +0.033 | +53.30€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2612 | +0.013 | +7.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2612 | +0.013 | +7.75€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1668 | +0.027 | +37.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1668 | +0.027 | +37.07€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7813 | +0.013 | -34.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7813 | +0.013 | -34.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3127 | +0.016 | -8.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3127 | +0.016 | -8.73€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3087 | +0.013 | -15.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3087 | +0.013 | -15.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1599 | +0.008 | -10.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1599 | +0.008 | -10.96€ | 2 | 0 |
| ✅ UPDOWN_GBM | 43283 | +0.035 | +2781.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11330 | +0.071 | +2131.30€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1552 | +0.004 | +6.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 27605 | +0.026 | +623.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2632 | +0.001 | +21.44€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4374 | +0.074 | +529.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 789 | +0.160 | +340.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3552 | +0.056 | +190.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8293 | +0.042 | +607.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1466 | +0.085 | +328.16€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 416 | +0.014 | +5.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5158 | +0.042 | +243.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1191 | +0.003 | +29.84€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 62 | -0.094 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4975 | +0.041 | +314.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 746 | +0.138 | +260.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4201 | +0.024 | +54.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9483 | +0.024 | +401.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2893 | +0.049 | +329.53€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 409 | +0.006 | +7.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5236 | +0.017 | +70.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 891 | -0.003 | -9.70€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 54 | -0.125 | +3.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9887 | +0.016 | +266.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2731 | +0.028 | +194.00€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 401 | -0.004 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6159 | +0.015 | +75.92€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 550 | +0.004 | +1.30€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 46 | -0.167 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6269 | +0.040 | +663.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2705 | +0.086 | +678.72€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 265 | -0.002 | -3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3299 | +0.005 | -11.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 162 | -0.128 | +0.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 598 | +0.350 | +197.25€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 598 | +0.350 | +197.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 330 | +0.355 | +107.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 330 | +0.355 | +107.16€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 268 | +0.341 | +90.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 268 | +0.341 | +90.10€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13111 | -0.036 | +2879.21€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13111 | -0.036 | +2879.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2406 | -0.122 | +31.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2406 | -0.122 | +31.33€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1491 | +0.208 | +917.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1491 | +0.208 | +917.03€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3941 | -0.064 | +584.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3941 | -0.064 | +584.05€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3915 | -0.073 | +638.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3915 | -0.073 | +638.56€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 152 | +0.039 | +8.44€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 152 | +0.039 | +8.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 152 | +0.039 | +8.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 152 | +0.039 | +8.44€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 968 | +0.291 | +774.30€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 968 | +0.291 | +774.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 528 | +0.287 | +401.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 528 | +0.287 | +401.11€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 440 | +0.294 | +373.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 440 | +0.294 | +373.19€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 738 | -0.112 | -84.25€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 738 | -0.112 | -84.25€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 218 | -0.082 | -16.25€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 218 | -0.082 | -16.25€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 71 | -0.199 | -8.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 71 | -0.199 | -8.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2597 | +0.300 | +1268.48€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 911 | +0.251 | +127.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 981 | +0.289 | +414.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 705 | +0.377 | +726.64€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.057) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=15303 | neutral: IC=+0.033 n=16075 | overbought(IBS>0.7): IC=+0.090 n=15509
  - _Datos_: n=48557 IC=+0.058 PNL=+6079.93€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 558 celda(s) pasan gate riguroso completo de 2309 evaluadas (n>=40) y 3289 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.028 < 0.08 — monitorear
  - _Datos_: n=2731 IC=+0.028 PNL=+194.00€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=981/15 IC=+0.289 PNL=+414.37€ | BTC: n=911/15 IC=+0.251 PNL=+127.47€ | SOL: n=705/15 IC=+0.377 PNL=+726.64€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 43221 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.124 n=389/60 | contraria IC=+0.170 n=365 | gap=-0.046 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=323, boost estimado=+0.012. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 187 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=891/40 IC=-0.003 PNL=-9.70€ | BTC#60min: n=1191/40 IC=+0.003 PNL=+29.84€ | SOL#60min: n=550/40 IC=+0.004 PNL=+1.30€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=371349 | tras_1loss IC=+0.082 n=287249 | tras_2loss IC=+0.052 n=119898/40 | gap=-0.003 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.017 n=5182 | contrario_BTC IC=+0.032 n=4605/40 | gap=+0.015 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.08 con n=364 PNL=+234.57€
  - _Datos_: n=364 IC=+0.186 PNL=+234.57€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=431 PNL=+323.62€
  - _Datos_: n=431 IC=+0.214 PNL=+323.62€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.245 > 0.08 con n=45 PNL=+34.88€
  - _Datos_: n=45 IC=+0.245 PNL=+34.88€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.327 > 0.1 con n=2123 PNL=+1155.66€
  - _Datos_: n=2123 IC=+0.327 PNL=+1155.66€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=343 IC=+0.059 PNL=+32.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=343 IC=+0.059 PNL=+32.76€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=56 IC=+0.190 PNL=+38.01€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=56 IC=+0.190 PNL=+38.01€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=41401 IC=+0.034 PNL=+2652.23€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=41401 IC=+0.034 PNL=+2652.23€

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
  - _Estado_: n=1826 IC=+0.005 PNL=-1.15€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1826 IC=+0.005 PNL=-1.15€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=806 IC=-0.009 PNL=+22.59€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=806 IC=-0.009 PNL=+22.59€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=558 IC=+0.027 PNL=+30.78€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=558 IC=+0.027 PNL=+30.78€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.1 con n=2410 PNL=+1539.13€
  - _Datos_: n=2410 IC=+0.187 PNL=+1539.13€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1359 IC=+0.055 PNL=+101.87€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1359 IC=+0.055 PNL=+101.87€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1466 IC=+0.085 PNL=+328.16€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1466 IC=+0.085 PNL=+328.16€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=6454 PNL=+1563.42€
  - _Datos_: n=6454 IC=+0.086 PNL=+1563.42€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=176 IC=-0.247 PNL=-5.12€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=176 IC=-0.247 PNL=-5.12€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=292 IC=-0.034 PNL=-0.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=292 IC=-0.034 PNL=-0.87€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=597 IC=+0.024 PNL=+45.25€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=597 IC=+0.024 PNL=+45.25€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=61 IC=+0.056 PNL=+3.99€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=61 IC=+0.056 PNL=+3.99€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6119 IC=-0.001 PNL=+2.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6119 IC=-0.001 PNL=+2.46€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=68 PNL=+18.45€
  - _Datos_: n=68 IC=+0.171 PNL=+18.45€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.262 n=107) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=107 IC=+0.262 PNL=+91.86€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=8043 IC=+0.038 PNL=+521.86€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8043 IC=+0.038 PNL=+521.86€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2703 IC=+0.057 PNL=+332.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2703 IC=+0.057 PNL=+332.59€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=392 PNL=+121.09€
  - _Datos_: n=392 IC=+0.112 PNL=+121.09€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.146 > 0.08 con n=677 PNL=+174.06€
  - _Datos_: n=677 IC=+0.146 PNL=+174.06€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=518 PNL=+249.83€
  - _Datos_: n=518 IC=+0.112 PNL=+249.83€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=60642 IC=+0.117 PNL=+22482.80€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=60642 IC=+0.117 PNL=+22482.80€

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
  - _Estado_: n=6475 IC=+0.040 PNL=+504.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6475 IC=+0.040 PNL=+504.25€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=696 PNL=+262.27€
  - _Datos_: n=696 IC=+0.119 PNL=+262.27€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=156 IC=-0.063 PNL=+31.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=156 IC=-0.063 PNL=+31.89€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.448 > 0.1 con n=1216 PNL=+1196.09€
  - _Datos_: n=1216 IC=+0.448 PNL=+1196.09€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=15631 IC=+0.055 PNL=+1875.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=15631 IC=+0.055 PNL=+1875.33€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=3927 PNL=+2149.41€
  - _Datos_: n=3927 IC=+0.202 PNL=+2149.41€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.149 < -0.1 con n=263 PNL=+28.43€
  - _Datos_: n=263 IC=-0.149 PNL=+28.43€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2085 IC=+0.053 PNL=+223.26€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2085 IC=+0.053 PNL=+223.26€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=89 IC=-0.115 PNL=+3.54€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=89 IC=-0.115 PNL=+3.54€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.1 con n=488 PNL=+136.72€
  - _Datos_: n=488 IC=+0.120 PNL=+136.72€

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
  - _Estado_: n=20154 IC=-0.137 PNL=+1387.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=20154 IC=-0.137 PNL=+1387.92€

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
  - _Estado_: n=2128 IC=+0.138 PNL=+1197.58€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2128 IC=+0.138 PNL=+1197.58€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=2371 PNL=+1526.49€
  - _Datos_: n=2371 IC=+0.189 PNL=+1526.49€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4528 IC=+0.024 PNL=+166.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4528 IC=+0.024 PNL=+166.39€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=2269 PNL=+1205.39€
  - _Datos_: n=2269 IC=+0.087 PNL=+1205.39€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.08 con n=533 PNL=+273.39€
  - _Datos_: n=533 IC=+0.208 PNL=+273.39€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.234 < -0.1 con n=1994 PNL=-200.99€
  - _Datos_: n=1994 IC=-0.234 PNL=-200.99€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=5905 IC=+0.174 PNL=+4036.50€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=5905 IC=+0.174 PNL=+4036.50€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=80 PNL=+31.30€
  - _Datos_: n=80 IC=+0.110 PNL=+31.30€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2161 IC=+0.066 PNL=+647.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2161 IC=+0.066 PNL=+647.46€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=1971 PNL=+1399.35€
  - _Datos_: n=1971 IC=+0.180 PNL=+1399.35€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3270 IC=-0.031 PNL=+864.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3270 IC=-0.031 PNL=+864.49€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=584 PNL=-53.91€
  - _Datos_: n=584 IC=+0.085 PNL=-53.91€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.235 > 0.08 con n=3536 PNL=-321.53€
  - _Datos_: n=3536 IC=+0.235 PNL=-321.53€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=40 IC=+0.000 PNL=+5.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=40 IC=+0.000 PNL=+5.94€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1139) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1139 IC=+0.101 PNL=+271.39€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.339 > 0.08 con n=296 PNL=+106.40€
  - _Datos_: n=296 IC=+0.339 PNL=+106.40€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=454) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=454 IC=+0.410 PNL=+639.66€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=9609 IC=+0.178 PNL=-1090.99€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9609 IC=+0.178 PNL=-1090.99€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.1 con n=153 PNL=+90.03€
  - _Datos_: n=153 IC=+0.197 PNL=+90.03€
