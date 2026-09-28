# Hipótesis automáticas — 2026-09-28 18:30 UTC
_Generado por shadow_postmortem.py sobre 654400 resoluciones (PNL=+76414.37€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=531)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=531)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.140 (n=170)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=438)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=396)

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

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 94.0 (IC base=+0.058)

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
- **FILTRO** `restante_s_al_confirmar` < `145.9` → IC=-0.218 (n=7516)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.9
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=22551)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.36` → IC=-0.246 (n=973)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.36
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=2919)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.92` → IC=-0.308 (n=884)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.92
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2655)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.14` → IC=-0.203 (n=1833)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.14
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=5505)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.5` → IC=-0.336 (n=1475)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.5
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=4425)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.230 (n=357)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=410)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.207 (n=14735)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3658)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5614.1784` → IC=+0.177 (n=2345)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5614.1784 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=12369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=15166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11726)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=5949)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7794.4204` → IC=+0.172 (n=2263)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7794.4204 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=1723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2225)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `15918.3154` → IC=+0.238 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15918.3154 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=1595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `15830.8412` → IC=+0.213 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15830.8412 (IC base=+0.197)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.176 (n=341)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.098)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=863)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.162 (n=226)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.101)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=2574)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.345 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.365 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.233 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `4232.2075` → IC=+0.230 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4232.2075 (IC base=+0.228)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.135 (n=718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.250 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=813)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1314.8555` → IC=+0.147 (n=711)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1314.8555 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.403 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.155 (n=1146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=757)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.154)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.176 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.370 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `1244.1621` → IC=+0.154 (n=232)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1244.1621 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.223 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.76` → IC=-0.289 (n=131)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=65)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=12540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=11980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.228 (n=4055)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `3571.1845` → IC=+0.331 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3571.1845 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=2841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.172 (n=2855)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=2857)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.251 (n=1041)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.341 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.246)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=2798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2819)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2384)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.251 (n=2602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.323 (n=845)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.197 (n=2151)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.463 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `11247.6748` → IC=+0.458 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11247.6748 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.445 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.457 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `14179.602` → IC=+0.446 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14179.602 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.449 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.462 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.425 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `3322.2122` → IC=+0.445 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.2122 (IC base=+0.427)

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
- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=37293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16506)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=6424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=6981)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=6715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=6694)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.263 (n=3809)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=6792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6778)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2468)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=6230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=2868)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5649)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.125 (n=5264)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=5314)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=6957)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.62` → IC=+0.139 (n=5248)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.62 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=2844)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.13` → IC=+0.125 (n=2611)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.13 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=2611)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.138 (n=3014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.29` → IC=+0.142 (n=2605)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.29 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=2805)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.127 (n=2649)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.2 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=2945)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=2647)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1545.7265` → IC=+0.294 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1545.7265 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.348 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `4262.2927` → IC=+0.296 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4262.2927 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1726.8276` → IC=+0.314 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1726.8276 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.350 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.344)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.344)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.385 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.344)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.439 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.434 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.438 (n=224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.434 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.454 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `1978.9685` → IC=+0.464 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9685 (IC base=+0.438)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4878` → IC=+0.126 (n=8836)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4878 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.9803` → IC=+0.243 (n=2947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9803 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2196` → IC=+0.258 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2196 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.342` → IC=+0.190 (n=2341)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.342 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.252 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `1.0466` → IC=+0.260 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0466 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.3022` → IC=+0.226 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3022 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.9003` → IC=+0.211 (n=4075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9003 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.5706` → IC=+0.134 (n=10696)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5706 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.606` → IC=+0.204 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.606 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.183 (n=1679)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6986 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `0.8696` → IC=+0.176 (n=2542)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8696 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.224 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.4504` → IC=+0.198 (n=6476)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4504 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.212 (n=6272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.067)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.196 (n=660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.175 (n=660)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0082 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.173 (n=1978)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1330)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.178` → IC=+0.269 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.178 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.207 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.169 (n=1858)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=1987)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.255 (n=696)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1252` → IC=+0.273 (n=675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1252 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.245 (n=1053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.289 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.497` → IC=+0.239 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.497 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.464` → IC=+0.245 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.464 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.267 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.5359` → IC=+0.237 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5359 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1812.1616` → IC=+0.237 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1812.1616 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.227 (n=1542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1116` → IC=+0.243 (n=678)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1116 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.238 (n=1543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8981` → IC=+0.266 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8981 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3466` → IC=+0.224 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3466 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.46` → IC=+0.268 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.46 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.223 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0813` → IC=+0.229 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0813 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.243 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7513` → IC=+0.221 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7513 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3804` → IC=+0.235 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3804 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11016.3169` → IC=+0.224 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11016.3169 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.175 (n=531)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.164 (n=528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.568` → IC=+0.174 (n=1392)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.568 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1296` → IC=+0.152 (n=1428)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1296 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.294` → IC=+0.151 (n=250)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.294 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.345` → IC=+0.143 (n=1453)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.345 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.148 (n=1582)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2085 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8572` → IC=+0.141 (n=1055)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8572 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.177 (n=419)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4311` → IC=+0.151 (n=1472)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4311 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4188` → IC=+0.144 (n=1472)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4188 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14020.0407` → IC=+0.144 (n=1055)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 14020.0407 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.170 (n=617)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 233.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.214 (n=658)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.192 (n=1974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1776)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.259 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.191 (n=1723)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.3555` → IC=+0.204 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3555 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.7734` → IC=+0.196 (n=1687)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7734 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2344)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.222 (n=1513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6264` → IC=+0.214 (n=1720)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6264 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0637` → IC=+0.240 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0637 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.703` → IC=+0.228 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.703 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.534` → IC=+0.212 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.534 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.261 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7532` → IC=+0.205 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7532 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1742` → IC=+0.216 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1742 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1910.02` → IC=+0.215 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.02 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.217 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.158 (n=109)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2395)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.139 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0037 (IC base=+0.034)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.219 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1948` → IC=+0.332 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1948 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.805` → IC=+0.168 (n=781)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.805 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8627` → IC=+0.339 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8627 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.333 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.352 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.336 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.331 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 157.0 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.661` → IC=+0.216 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.661 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.154 (n=629)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.852 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1641` → IC=+0.155 (n=314)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1641 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2309` → IC=+0.211 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2309 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.168 (n=794)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.021)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=358)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.194 (n=106)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=319)

- **FILTRO** `ibs_20min` > `0.2472` → IC=-0.125 (n=2389)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2472
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=1177)

- **FILTRO** `sigma_ewma_delta_pct` > `8.705` → IC=-0.216 (n=379)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.705
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3187)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.170 (n=213)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6111 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `1.8814` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.8814 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.5572` → IC=+0.277 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5572 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.291 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.2472` → IC=+0.126 (n=1177)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2472 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7328` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7328 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.4545` → IC=+0.232 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4545 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6732` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6732 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1591` → IC=+0.286 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1591 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.283 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6579` → IC=-0.181 (n=621)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6579
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1871)

- **FILTRO** `ibs_20min` < `0.7191` → IC=-0.154 (n=1644)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7191
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=848)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=524)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1968)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.208 (n=911)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2778)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.315 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2822` → IC=+0.314 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2822 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.310 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.301 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.4256` → IC=+0.300 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4256 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.298 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.5647` → IC=+0.277 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5647 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` < `0.733` → IC=+0.252 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.733 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` > `1.0829` → IC=+0.274 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0829 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1004` → IC=+0.263 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1004 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.1331` → IC=+0.262 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1331 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5229` → IC=+0.248 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5229 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.197 (n=3760)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0098 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4741` → IC=+0.186 (n=10074)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4741 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `1.0215` → IC=+0.290 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0215 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.625` → IC=+0.159 (n=5232)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.625 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.6911` → IC=+0.254 (n=3607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6911 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2931` → IC=+0.272 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2931 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.4637` → IC=+0.243 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4637 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.6527` → IC=+0.251 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6527 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.272 (n=6072)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.166 (n=3688)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0092 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.153 (n=9743)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.55 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7124` → IC=+0.248 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7124 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2498` → IC=+0.245 (n=3163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2498 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7096` → IC=+0.246 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7096 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.2049` → IC=+0.251 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2049 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.303 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.595` → IC=+0.266 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.595 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.2826` → IC=+0.262 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2826 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.273 (n=4325)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2558` → IC=-0.152 (n=779)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2558
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2338)

- **FILTRO** `sigma_ewma_delta_pct` > `4.536` → IC=-0.167 (n=590)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.536
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1966)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.273 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.851` → IC=+0.210 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.851 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.263 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.190 (n=333)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.1694` → IC=+0.212 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1694 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.207 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.2144` → IC=+0.455 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2144 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.7555` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7555 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.473 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8659` → IC=+0.168 (n=756)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8659 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.178 (n=399)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6758` → IC=+0.179 (n=934)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6758 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.201 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4012` → IC=+0.174 (n=342)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4012 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.205 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 236.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.221 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.232 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8596 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.302 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.238 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `458.0` → IC=+0.219 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 458.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.290 (n=584)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=1758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=1771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.725` → IC=+0.284 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.725 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.262 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `3.3191` → IC=+0.268 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3191 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2056)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1912.1584` → IC=+0.258 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1584 (IC base=+0.249)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.311 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.6231` → IC=+0.287 (n=1429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6231 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.291 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.682` → IC=+0.292 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.682 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.707` → IC=+0.284 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.707 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3387` → IC=+0.296 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3387 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.5856` → IC=+0.292 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5856 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.6923` → IC=+0.290 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6923 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1903.2584` → IC=+0.298 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.2584 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.289 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.773` → IC=-0.184 (n=660)

  - _Acción_: SKIP cuando `ibs_20min` > 0.773
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1983)

- **PATRÓN** `ibs_20min` > `0.9124` → IC=+0.179 (n=565)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.9124 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.1824` → IC=+0.229 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1824 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.9991` → IC=+0.247 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9991 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.224 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.261 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.267 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.7573` → IC=+0.238 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7573 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.254 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.1485` → IC=+0.222 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1485 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `1.1663` → IC=+0.217 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1663 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.238 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.258 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8106 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1238` → IC=+0.251 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1238 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.264 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.193 (n=1194)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.279 (n=1199)

- **FILTRO** `ibs_20min` > `0.6818` → IC=-0.233 (n=602)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6818
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1814)

- **FILTRO** `sigma_ewma_delta_pct` > `4.739` → IC=-0.192 (n=527)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.739
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1889)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.279 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.8467` → IC=+0.325 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8467 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.65` → IC=+0.170 (n=377)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.65 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8642` → IC=+0.307 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8642 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.642` → IC=+0.297 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.642 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1013` → IC=+0.297 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1013 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2703` → IC=+0.300 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2703 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.328 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.321 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.5806` → IC=+0.124 (n=1596)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.5806 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.2971` → IC=+0.229 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2971 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.258 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.222 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.231 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.240 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.245 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.017)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.316 (n=955)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.297 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.7388` → IC=+0.324 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7388 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.315 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.658` → IC=+0.305 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.658 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.309 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.329 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.290 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2460.6024` → IC=+0.289 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2460.6024 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.321 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.308 (n=1019)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.1979` → IC=+0.283 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1979 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.289 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.281 (n=762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.2907` → IC=+0.316 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2907 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.316` → IC=+0.287 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.316 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.2297` → IC=+0.279 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2297 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.08` → IC=+0.296 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.08 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.281 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.308 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.331 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.289 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.1376` → IC=+0.275 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1376 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2404.3655` → IC=+0.283 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.3655 (IC base=+0.278)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.179 (n=2873)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0049 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.203 (n=2863)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3603` → IC=+0.177 (n=7552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3603 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=8981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.220 (n=8585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1755` → IC=+0.194 (n=3683)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1755 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.255 (n=1747)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.164 (n=5699)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2075 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6298` → IC=+0.161 (n=5698)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6298 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2422` → IC=+0.197 (n=1732)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2422 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5587` → IC=+0.169 (n=3628)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5587 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6099` → IC=+0.177 (n=2749)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6099 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1947.8684` → IC=+0.171 (n=7666)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1947.8684 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.183 (n=7498)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 110.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.183 (n=5501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0067 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.212 (n=2753)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=3934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4836` → IC=+0.225 (n=8251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4836 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.2364` → IC=+0.161 (n=6001)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2364 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.194 (n=1397)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.1765` → IC=+0.154 (n=5938)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1765 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.213 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5608` → IC=+0.169 (n=3330)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5608 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6198` → IC=+0.171 (n=2521)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6198 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.177 (n=7213)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 110.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.221 (n=486)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.189 (n=484)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0083 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.211 (n=1449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=1531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=969)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.18` → IC=+0.329 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.18 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2305` → IC=+0.239 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2305 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.186 (n=1346)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.239 (n=962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.248 (n=974)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1842` → IC=+0.290 (n=727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1842 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.244 (n=1051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=1009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3469` → IC=+0.257 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3469 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.288` → IC=+0.249 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.288 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.234 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.247 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.262 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1814.1` → IC=+0.245 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1814.1 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.241 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.199 (n=426)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=1284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.3965` → IC=+0.228 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3965 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.211 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.468` → IC=+0.238 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.468 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.688` → IC=+0.175 (n=562)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.688 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.0753` → IC=+0.168 (n=580)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0753 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.203 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.181 (n=546)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.168 (n=414)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `10568.6415` → IC=+0.171 (n=1278)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10568.6415 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `442.0` → IC=+0.163 (n=1199)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 442.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.157 (n=1372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0057 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.162 (n=1369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5802` → IC=+0.187 (n=1369)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5802 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.161 (n=1369)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.204 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.156 (n=1369)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2116 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.151 (n=419)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.146 (n=1258)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4262` → IC=+0.135 (n=1257)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4262 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.165 (n=395)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 213.0 (IC base=+0.137)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.219 (n=652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2418` → IC=+0.219 (n=958)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2418 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.280 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2024` → IC=+0.208 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2024 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.799` → IC=+0.199 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.799 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.7741` → IC=+0.217 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7741 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.235 (n=1077)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1003` → IC=+0.254 (n=408)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1003 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.245 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.685` → IC=+0.249 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.685 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3553` → IC=+0.253 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3553 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7564` → IC=+0.221 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7564 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `3.3626` → IC=+0.236 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3626 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1905.7248` → IC=+0.220 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1905.7248 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.213 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.178 (n=1210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0066 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4277` → IC=+0.161 (n=1374)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4277 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9441` → IC=+0.278 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9441 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1517` → IC=+0.177 (n=897)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1517 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.227 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.157 (n=918)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.856 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.147 (n=1374)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6209 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.199 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.161 (n=449)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.167 (n=449)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5397.129` → IC=+0.185 (n=916)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5397.129 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.150 (n=1311)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 159.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.153 (n=1445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.381` → IC=+0.144 (n=1444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.381 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6509` → IC=+0.171 (n=1444)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6509 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.963` → IC=+0.163 (n=511)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.963 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8528` → IC=+0.148 (n=963)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8528 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.179 (n=216)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.8136` → IC=+0.139 (n=881)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8136 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9873.0554` → IC=+0.167 (n=655)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9873.0554 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.122 (n=1258)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 156.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.152 (n=710)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0101 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.204 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.8396` → IC=+0.208 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8396 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.733` → IC=+0.254 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.733 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2054` → IC=+0.132 (n=1565)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2054 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.126 (n=1571)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.125 (n=660)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5431` → IC=+0.137 (n=665)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5431 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1626)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2878.9982` → IC=+0.195 (n=710)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2878.9982 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.139 (n=1207)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 48.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.158 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0062 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1034` → IC=+0.168 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1034 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.212 (n=1591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0169` → IC=+0.131 (n=220)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 1.0169 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.144 (n=1462)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.137` → IC=+0.133 (n=257)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.137 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.148 (n=532)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6381 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.156 (n=280)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.141 (n=480)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.133 (n=480)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2736.5522` → IC=+0.164 (n=721)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2736.5522 (IC base=+0.117)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.227 (n=1325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.1355` → IC=+0.204 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1355 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7381` → IC=+0.261 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7381 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.5175` → IC=+0.218 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5175 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.242 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2039` → IC=+0.207 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2039 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6301` → IC=+0.214 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6301 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.267 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.1453` → IC=+0.214 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1453 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4077` → IC=+0.211 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4077 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2924.9554` → IC=+0.204 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2924.9554 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.224 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.220 (n=697)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.228 (n=513)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.0205` → IC=+0.299 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0205 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `1.2245` → IC=+0.224 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2245 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.392` → IC=+0.244 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.392 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6331` → IC=+0.215 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6331 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.279 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.1921` → IC=+0.199 (n=1225)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1921 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4295` → IC=+0.202 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4295 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2376.977` → IC=+0.212 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2376.977 (IC base=+0.206)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.169 (n=725)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0087 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.3432` → IC=+0.165 (n=1913)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3432 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.5182` → IC=+0.193 (n=1941)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5182 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.8241` → IC=+0.178 (n=346)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.8241 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.1518` → IC=+0.160 (n=1608)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1518 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.734` → IC=+0.186 (n=969)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.734 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.180 (n=1293)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.8725 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.161 (n=647)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.2084 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.173 (n=595)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.170 (n=701)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.539` → IC=+0.167 (n=701)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.539 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=2456)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `2202.4322` → IC=+0.162 (n=2173)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2202.4322 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.175 (n=1951)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 148.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.137 (n=1485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0057 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3455` → IC=+0.128 (n=1961)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3455 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=2235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.0596` → IC=+0.187 (n=743)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0596 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2135` → IC=+0.121 (n=2019)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2135 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2259` → IC=+0.121 (n=2023)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2259 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.137 (n=551)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4469` → IC=+0.144 (n=718)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4469 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2755.5763` → IC=+0.123 (n=1990)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2755.5763 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.131 (n=929)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 28.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.155 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0039 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3302` → IC=+0.146 (n=544)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3302 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.174 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.656` → IC=+0.204 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.656 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.2887` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.2887 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1618` → IC=+0.134 (n=479)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1618 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.181` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.181 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6213` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6213 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` < `0.1564` → IC=+0.130 (n=563)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1564 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0914` → IC=+0.146 (n=193)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0914 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.2101` → IC=+0.137 (n=466)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2101 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.5102` → IC=+0.134 (n=473)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5102 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `10581.1275` → IC=+0.146 (n=544)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 10581.1275 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.159 (n=344)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 230.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.155 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.181 (n=606)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6119 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.3107` → IC=+0.148 (n=733)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.3107 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.421` → IC=+0.145 (n=260)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 4.421 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.177` → IC=+0.136 (n=627)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.177 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.141 (n=688)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2216 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.7161` → IC=+0.148 (n=615)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7161 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1128` → IC=+0.159 (n=597)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1128 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.143 (n=678)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `316.0` → IC=+0.147 (n=578)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 316.0 (IC base=+0.134)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.273 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.218 (n=456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.9601` → IC=+0.270 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9601 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.208 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.208 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.949` → IC=+0.231 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.949 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.214 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.226 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.154` → IC=+0.251 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.154 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4064` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4064 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.1032` → IC=+0.240 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1032 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.0839` → IC=+0.151 (n=213)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0839 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6887` → IC=+0.136 (n=281)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6887 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.146 (n=478)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0059 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.5376` → IC=+0.135 (n=535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.5376 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.169 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.9873` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9873 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.191 (n=286)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.157 (n=470)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.069 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.7219` → IC=+0.138 (n=478)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.7219 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.482` → IC=+0.144 (n=172)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.482 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.212` → IC=+0.164 (n=233)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.212 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=557)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3102.4168` → IC=+0.194 (n=178)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3102.4168 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.121 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 13.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.4189` → IC=+0.166 (n=435)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.4189 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.22` → IC=+0.122 (n=495)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.22 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.5789` → IC=+0.183 (n=206)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5789 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2917.7847` → IC=+0.156 (n=225)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2917.7847 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.142 (n=445)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 40.0 (IC base=+0.099)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.176 (n=3701)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.208 (n=3698)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=11605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.9984` → IC=+0.309 (n=3697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9984 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.9388` → IC=+0.200 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9388 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.343` → IC=+0.246 (n=2781)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.343 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.88` → IC=+0.170 (n=4951)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.88 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.201 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5899` → IC=+0.193 (n=3565)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5899 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1786.74` → IC=+0.176 (n=11091)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1786.74 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.199 (n=8568)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 83.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.15` → IC=+0.190 (n=4417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.15 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=4655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4512` → IC=+0.246 (n=8832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4512 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2517` → IC=+0.161 (n=6272)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2517 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.063` → IC=+0.199 (n=1409)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.063 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.734` → IC=+0.183 (n=9710)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.734 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.162 (n=3017)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7053 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.241 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6101` → IC=+0.191 (n=3093)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6101 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.198 (n=5955)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 46.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=623)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.219 (n=620)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.197 (n=1858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=1258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.6` → IC=+0.347 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.6 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2278` → IC=+0.249 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2278 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.5623` → IC=+0.201 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5623 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.260 (n=656)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.127` → IC=+0.287 (n=656)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.127 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=1348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3559` → IC=+0.282 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3559 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.502` → IC=+0.263 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.502 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.287 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.5478` → IC=+0.257 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5478 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.277 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1809.64` → IC=+0.265 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1809.64 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.204 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1128` → IC=+0.164 (n=781)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1128 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3055` → IC=+0.206 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3055 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1263` → IC=+0.186 (n=989)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1263 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.176 (n=402)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.15` → IC=+0.155 (n=1608)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.15 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.186 (n=593)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6273 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2657` → IC=+0.195 (n=257)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2657 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.1148` → IC=+0.163 (n=1513)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.1148 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.159 (n=1146)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `11191.459` → IC=+0.161 (n=1586)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11191.459 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `470.0` → IC=+0.164 (n=1653)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 470.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1525)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3206` → IC=+0.160 (n=1525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3206 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.2856` → IC=+0.232 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2856 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6698` → IC=+0.156 (n=242)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6698 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1325` → IC=+0.161 (n=1395)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1325 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.518` → IC=+0.164 (n=254)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.518 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.151 (n=1389)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.194` → IC=+0.161 (n=1525)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.194 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.197 (n=404)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.158 (n=1427)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7569` → IC=+0.160 (n=951)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7569 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `415.0` → IC=+0.151 (n=1171)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 415.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.257 (n=603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.305 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.1344` → IC=+0.219 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1344 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.227 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1915.5084` → IC=+0.224 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.5084 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.238 (n=1693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1776` → IC=+0.240 (n=745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1776 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.3586` → IC=+0.263 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3586 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.766` → IC=+0.269 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.766 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.300 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7398` → IC=+0.230 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7398 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1571` → IC=+0.236 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1571 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1906.4295` → IC=+0.243 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1906.4295 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.253 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.187 (n=833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.433` → IC=+0.152 (n=1893)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.433 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=1979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8695` → IC=+0.262 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8695 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3627` → IC=+0.161 (n=730)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3627 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.515` → IC=+0.169 (n=309)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.515 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.160 (n=1263)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8725 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2798` → IC=+0.213 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2798 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.156 (n=808)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.4714` → IC=+0.156 (n=612)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4714 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7789.4103` → IC=+0.236 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7789.4103 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.173 (n=598)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 75.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.166 (n=1027)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0052 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.146 (n=1537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.1502` → IC=+0.260 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1502 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.135 (n=1342)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.273` → IC=+0.162 (n=229)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.273 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6983` → IC=+0.148 (n=677)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6983 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.2011` → IC=+0.141 (n=513)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.2011 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.232 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.444` → IC=+0.144 (n=1464)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.444 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6979.8882` → IC=+0.192 (n=697)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6979.8882 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.137 (n=1462)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 172.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.139 (n=1258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0082 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.192 (n=1889)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4615 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0841` → IC=+0.203 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0841 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.529` → IC=+0.241 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.529 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.8911` → IC=+0.141 (n=1258)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8911 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1900)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2883.9504` → IC=+0.254 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2883.9504 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.136 (n=1480)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 53.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.174 (n=606)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0058 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.157 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.6371` → IC=+0.205 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6371 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.133 (n=1487)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.454` → IC=+0.127 (n=1747)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.454 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.156 (n=797)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7144 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.169 (n=282)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.143 (n=550)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2760.8425` → IC=+0.177 (n=604)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2760.8425 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.126 (n=1437)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 51.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0272` → IC=+0.213 (n=1874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0272 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.230 (n=1673)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2152` → IC=+0.234 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2152 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.253 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2457` → IC=+0.214 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2457 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.223 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2322` → IC=+0.246 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2322 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.5468` → IC=+0.222 (n=1619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5468 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2434.1618` → IC=+0.219 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2434.1618 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.221 (n=661)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.018` → IC=+0.220 (n=1322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.018 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.216 (n=1397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4224` → IC=+0.264 (n=1745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4224 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.2326` → IC=+0.207 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2326 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2162` → IC=+0.211 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2162 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.258 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.236` → IC=+0.238 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.236 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.272 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1751` → IC=+0.203 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1751 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4266` → IC=+0.202 (n=1796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4266 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2381.856` → IC=+0.207 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2381.856 (IC base=+0.205)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=3401)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.185 (n=2981)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0092 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.5129` → IC=+0.182 (n=3387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.5129 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=1304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.177 (n=1518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.235 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1848` → IC=+0.182 (n=1219)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1848 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.4754` → IC=+0.168 (n=2145)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.4754 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.157` → IC=+0.200 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.157 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.167 (n=990)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7067 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.892` → IC=+0.175 (n=1500)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.892 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1701` → IC=+0.203 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1701 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.181 (n=1117)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.869` → IC=+0.179 (n=2230)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.869 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=2413)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2818.949` → IC=+0.174 (n=3026)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2818.949 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.202 (n=859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.4894` → IC=+0.171 (n=2563)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.4894 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.174 (n=1142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.181 (n=1129)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.18 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6833` → IC=+0.175 (n=469)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6833 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.207` → IC=+0.164 (n=2562)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.207 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.1012` → IC=+0.162 (n=2117)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1012 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.159 (n=2335)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5388` → IC=+0.164 (n=1114)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5388 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8237` → IC=+0.161 (n=1688)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8237 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=3401)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `12357.2708` → IC=+0.160 (n=854)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12357.2708 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.160 (n=1664)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 86.0 (IC base=+0.154)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.181 (n=424)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1409 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6109` → IC=+0.146 (n=436)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6109 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.162 (n=942)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8794` → IC=+0.187 (n=641)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8794 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0686` → IC=+0.166 (n=447)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0686 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.146 (n=320)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.150 (n=639)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14904.1418` → IC=+0.160 (n=436)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 14904.1418 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.144 (n=916)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 707.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.187 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.178 (n=284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.01 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.5778` → IC=+0.172 (n=627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.5778 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.732` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.732 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.3498` → IC=+0.168 (n=754)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.3498 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.201 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.6744` → IC=+0.168 (n=209)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.6744 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.168 (n=559)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2426.4931` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2426.4931 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.324 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.266 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` > `0.2025` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2025 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.258)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.183 (n=928)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0072 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3745` → IC=+0.181 (n=928)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3745 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.183 (n=361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 4.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.190 (n=704)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5305 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.8825` → IC=+0.184 (n=352)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8825 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.182 (n=876)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.19` → IC=+0.185 (n=943)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.19 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0828` → IC=+0.176 (n=928)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0828 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.177 (n=1055)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6398 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.194 (n=318)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.4754` → IC=+0.180 (n=1036)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4754 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.176 (n=927)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1051)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.202 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.183 (n=860)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.161 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.161 (n=861)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.7466 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.0945` → IC=+0.164 (n=860)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.0945 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.6041` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6041 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.399` → IC=+0.165 (n=781)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.399 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.647` → IC=+0.196 (n=287)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.647 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.157 (n=768)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7253 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.175 (n=364)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.171 (n=742)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7861.9245` → IC=+0.177 (n=768)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7861.9245 (IC base=+0.156)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.161 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0109 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3752` → IC=+0.137 (n=213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3752 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.163 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 4.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.139 (n=322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 14.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.95` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.95 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2235` → IC=+0.194 (n=217)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.2235 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.026` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.026 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8829` → IC=+0.170 (n=213)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8829 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5377` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5377 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.424` → IC=+0.156 (n=309)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.424 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=377)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3055.3138` → IC=+0.157 (n=319)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3055.3138 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.155 (n=265)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 53.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.184 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0069 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.198 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.179 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 10.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.2647` → IC=+0.227 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2647 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.669` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.669 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.258` → IC=+0.165 (n=261)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 5.258 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.756` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.756 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.224 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.522` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.522 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3214.2568` → IC=+0.195 (n=270)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3214.2568 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.200 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.154)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.196 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=416)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.170 (n=461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.188 (n=847)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.6494 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1475` → IC=+0.144 (n=504)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1475 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.428` → IC=+0.189 (n=220)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.428 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.188 (n=126)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.081)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.124 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0045 (IC base=+0.029)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.301 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.134 (n=383)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.121` → IC=+0.139 (n=128)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.121 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.138` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.138 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.139 (n=278)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.437` → IC=+0.136 (n=248)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.437 (IC base=+0.029)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=287)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.029)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.144 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0058 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4669` → IC=+0.181 (n=327)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4669 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.176 (n=168)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.141 (n=288)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.097)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.133 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0044 (IC base=+0.076)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.0673` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0673 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.557` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 4.557 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `1.1209` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1209 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0669` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0669 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.076)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6632` → IC=-0.134 (n=140)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6632
  - _Potencial_: sin este filtro IC_bueno=+0.215 (n=286)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=134)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.140 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0049 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.6632` → IC=+0.215 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6632 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.3362` → IC=+0.182 (n=124)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3362 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `1128.1831` → IC=+0.148 (n=282)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1128.1831 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1283` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1283 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.256` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.256 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.3281` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.3281 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.1925` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.1925 (IC base=+0.009)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.009)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.265 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=98)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.236 (n=70)

- **PATRÓN** `ibs_20min` > `0.7843` → IC=+0.186 (n=202)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7843 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.054)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.145 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0066 (IC base=-0.024)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=-0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1002` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1002 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4839` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.4839 (IC base=-0.024)

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

- **FILTRO** `sigma_h` > `0.005` → IC=-0.357 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=121)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.305 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=143)

- **FILTRO** `dist_vwap_pct` > `0.338` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.338
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=150)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=152)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=80)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.250 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=30)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

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
- **FILTRO** `ibs_20min` > `0.1667` → IC=-0.132 (n=131)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=257)

- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=362)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.162 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0059 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6422` → IC=+0.148 (n=282)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6422 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.51` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.51 (IC base=+0.082)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.126 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.004 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.176 (n=257)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1667 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.072)

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

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.170 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0034 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.101` → IC=+0.217 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.101 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.0646` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.0646 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.611` → IC=+0.145 (n=108)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.611 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.138` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.138 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.2815` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.2815 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.133)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6191` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6191
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=77)

- **FILTRO** `volumen_pendiente_norm` > `0.0671` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0671
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=42)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=84)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.010)

- **PATRÓN** `ibs_20min` > `0.8782` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.8782 (IC base=+0.010)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.010)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.122 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1644 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.8247` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8247 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.062)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_regimen` < `1.0341` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0341
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.250 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.245 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.219)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=797)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2903.137` → IC=+0.158 (n=273)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2903.137 (IC base=+0.106)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=797)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2903.137` → IC=+0.158 (n=273)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2903.137 (IC base=+0.106)

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
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=219)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=205)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=44)

- **FILTRO** `libro_liquidez` < `10452.0502` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 10452.0502
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

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

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=89)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1983)

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

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=87)

- **PATRÓN** `libro_liquidez` > `2413.9166` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2413.9166 (IC base=+0.040)

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

  - _Acción_: Kelly boost +0.97€ cuando `liq_n` > 18.0 (IC base=+0.016)

- **PATRÓN** `liq_usd_total` > `68754.71` → IC=+0.158 (n=109)

  - _Acción_: Kelly boost +0.79€ cuando `liq_usd_total` > 68754.71 (IC base=+0.016)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=147)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=861)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=815)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=454)

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
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=672)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=672)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=408)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=408)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=179)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=179)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=116)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=223)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=100)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=103)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=255)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=255)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.152 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=218)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=145)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.134 (n=364)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=938)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.130 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=118)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.52 (IC base=+0.022)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.129 (n=122)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.59 (IC base=+0.067)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **FILTRO** `restante_min` > `13.33` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `restante_min` > 13.33
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.267 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.146 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 9.0 (IC base=+0.086)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `profundidad_ratio` < `50.1` → IC=-0.222 (n=34)

  - _Acción_: SKIP cuando `profundidad_ratio` < 50.1
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=72)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=101)

- **FILTRO** `profundidad_ratio` < `19.0` → IC=-0.143 (n=40)

  - _Acción_: SKIP cuando `profundidad_ratio` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=83)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.018)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.46 (IC base=-0.012)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=114)

- **FILTRO** `restante_min` < `3.46` → IC=-0.292 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 3.46
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=95)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.233 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=98)

- **FILTRO** `lag_apertura_s` > `91.82` → IC=-0.296 (n=47)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.82
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=94)

- **FILTRO** `profundidad_ratio` < `74.6` → IC=-0.236 (n=70)

  - _Acción_: SKIP cuando `profundidad_ratio` < 74.6
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=71)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.44 (IC base=+0.062)

- **PATRÓN** `profundidad_ratio` > `26.3` → IC=+0.132 (n=85)

  - _Acción_: Kelly boost +0.66€ cuando `profundidad_ratio` > 26.3 (IC base=+0.062)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `restante_min` > `13.47` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 13.47 (IC base=-0.022)

- **PATRÓN** `lag_apertura_s` < `91.34` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 91.34 (IC base=-0.022)

- **PATRÓN** `restante_min` > `13.42` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 13.42 (IC base=+0.012)

- **PATRÓN** `lag_apertura_s` < `91.0` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 91.0 (IC base=+0.012)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `restante_min` < `3.76` → IC=-0.123 (n=59)

  - _Acción_: SKIP cuando `restante_min` < 3.76
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=61)

- **FILTRO** `lag_apertura_s` > `74.64` → IC=-0.123 (n=59)

  - _Acción_: SKIP cuando `lag_apertura_s` > 74.64
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=61)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.125 (n=102)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=57)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.5 (IC base=-0.022)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.250 (n=54)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=132)

- **FILTRO** `restante_min` < `2.81` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 2.81
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=140)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=140)

- **FILTRO** `lag_apertura_s` > `131.11` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `lag_apertura_s` > 131.11
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=140)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=3848)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=11853)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.161 (n=4002)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=12297)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.202 (n=666)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=2082)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.186 (n=686)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2112)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=700)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=2236)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.171 (n=672)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=2067)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.173 (n=723)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2212)

- **PATRÓN** `libro_liquidez` > `2576.7572` → IC=+0.121 (n=932)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2576.7572 (IC base=+0.022)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2222)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2325)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3065)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=409)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=400)

- **FILTRO** `libro_liquidez` < `17011.7455` → IC=-0.143 (n=228)

  - _Acción_: SKIP cuando `libro_liquidez` < 17011.7455
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=685)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=260)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=260)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `drift_20min_pct` |x|> `0.2312` → IC=-0.120 (n=322)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2312
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=626)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=10972)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=24701)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=8833)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=26840)

- **FILTRO** `ibs_7min` < `0.274` → IC=-0.235 (n=8916)

  - _Acción_: SKIP cuando `ibs_7min` < 0.274
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=26757)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=11939)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=23734)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.231 (n=11041)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=34065)

- **FILTRO** `ibs_7min` > `0.2917` → IC=-0.177 (n=11254)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33852)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=1790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4179)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1415)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4554)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.254 (n=1967)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=4002)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.175 (n=1455)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4514)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.261 (n=1925)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=5830)

- **FILTRO** `ibs_7min` > `0.788` → IC=-0.207 (n=1938)

  - _Acción_: SKIP cuando `ibs_7min` > 0.788
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=5817)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=4699)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1497)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4639)

- **FILTRO** `ibs_7min` < `0.7461` → IC=-0.198 (n=1534)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7461
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4602)

- **FILTRO** `ballena_activa_n` > `158.0` → IC=-0.179 (n=1526)

  - _Acción_: SKIP cuando `ballena_activa_n` > 158.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4610)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1444)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4804)

- **FILTRO** `ibs_7min` > `0.2614` → IC=-0.185 (n=1561)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2614
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4687)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.181 (n=1561)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4687)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.170 (n=1385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4287)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.304 (n=1412)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4260)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.244 (n=1864)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3808)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.210 (n=1396)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4276)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=1918)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=6398)

- **FILTRO** `ibs_7min` > `0.7467` → IC=-0.174 (n=2078)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7467
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6238)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=1885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3989)

- **FILTRO** `ibs_7min` < `0.7409` → IC=-0.182 (n=1468)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7409
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4406)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.174 (n=1430)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=4444)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.256 (n=1507)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4532)

- **FILTRO** `ibs_7min` > `0.2759` → IC=-0.175 (n=1508)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4531)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.181 (n=1491)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4548)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.261 (n=1440)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4701)

- **FILTRO** `ibs_7min` < `0.2821` → IC=-0.232 (n=1533)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4608)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.168 (n=2146)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=6457)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1441)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4440)

- **FILTRO** `ibs_7min` < `0.29` → IC=-0.224 (n=1469)

  - _Acción_: SKIP cuando `ibs_7min` < 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4412)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1397)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4484)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.207 (n=1904)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6241)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1145)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=568)

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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=574)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.132 (n=807)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.142 (n=269)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 469.512 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4061` → IC=+0.133 (n=164)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.4061 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.199 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.134 (n=162)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 445.688 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2333.2912` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2333.2912 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 14.0 (IC base=+0.130)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 8.0 (IC base=+0.108)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.175 (n=112)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.124 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.098)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 75.0 (IC base=+0.098)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.176 (n=140)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.235 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `6163.256` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 6163.256 (IC base=+0.133)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.146 (n=145)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.135 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 13.0 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.105)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.323 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=282)

- **FILTRO** `T_h` > `51.9942` → IC=-0.240 (n=286)

  - _Acción_: SKIP cuando `T_h` > 51.9942
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=141)

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

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.8113` → IC=-0.238 (n=105)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8113
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=316)

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
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=203)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=310)

- **FILTRO** `streak_estiramiento` > `0.8486` → IC=-0.167 (n=67)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8486
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=202)

- **PATRÓN** `streak_estiramiento` < `0.4787` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.4787 (IC base=+0.036)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.031)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=19)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `2331737.7` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 2331737.7
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=46)

- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=37)

- **PATRÓN** `streak_estiramiento` < `0.479` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.479 (IC base=-0.008)

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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=434)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `libro_liquidez` < `2775.6672` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2775.6672
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `streak_estiramiento` > `0.9124` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.9124
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=666)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1223)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=819)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=796)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3099)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1561)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1569)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.193 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0043 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.227 (n=602)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.202 (n=601)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2173` → IC=+0.192 (n=601)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2173 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.234 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=1693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.189 (n=1876)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.6077` → IC=+0.267 (n=1802)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6077 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.184 (n=904)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.836` → IC=+0.272 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.836 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `8758.4418` → IC=+0.197 (n=601)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 8758.4418 (IC base=+0.188)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=746)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.222 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.285 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.209)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.248 (n=133)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.209)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.282 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.209)

- **PATRÓN** `ibs_15` > `0.7061` → IC=+0.276 (n=399)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7061 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.537` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.537 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `16060.5409` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16060.5409 (IC base=+0.209)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.723` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.723
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=454)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.174 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0035 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.135 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.005 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.156 (n=187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.174 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.131)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.162 (n=155)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.6559` → IC=+0.253 (n=379)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6559 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.142 (n=336)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.218 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4165.118` → IC=+0.142 (n=283)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4165.118 (IC base=+0.131)

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
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1132)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.271 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.225 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0403` → IC=+0.200 (n=465)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0403 (IC base=+0.196)

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

- **PATRÓN** `dist_vwap_pct` < `0.8342` → IC=+0.199 (n=539)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.8342 (IC base=+0.196)

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
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.357 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.349)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.374 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.349)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.351 (n=300)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.349)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.362 (n=446)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=+0.349)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.388 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.349)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.349)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.389 (n=447)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.349)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.390 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.352 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.349)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.352 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.349)

- **PATRÓN** `libro_liquidez` > `3805.841` → IC=+0.365 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3805.841 (IC base=+0.349)

- **PATRÓN** `ballena_activa_n` < `457.0` → IC=+0.370 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 457.0 (IC base=+0.349)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.363 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.381 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.371 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.354)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.365 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0763` → IC=+0.363 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0763 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.387 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.405 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.358 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `11121.9309` → IC=+0.373 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11121.9309 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `571.0` → IC=+0.400 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 571.0 (IC base=+0.354)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.382 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.340)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.346 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.340)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.362 (n=179)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.340)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.370 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.406 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.340)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.392 (n=201)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.377 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.350 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1175 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.347 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `4305.62` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4305.62 (IC base=+0.340)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.349 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.340)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.224 (n=711)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2137)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.204 (n=986)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1862)

- **FILTRO** `libro_liquidez` < `3078.9133` → IC=-0.145 (n=1424)

  - _Acción_: SKIP cuando `libro_liquidez` < 3078.9133
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1424)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.249 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6389` → IC=+0.270 (n=681)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6389 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2713` → IC=+0.188 (n=550)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2713 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0775` → IC=+0.245 (n=1804)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0775 (IC base=-0.028)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.242 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.028)

- **PATRÓN** `ibs_15` < `0.3514` → IC=+0.273 (n=2020)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3514 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.687` → IC=+0.296 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.687 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.214 (n=432)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=1298)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.226 (n=570)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1160)

- **FILTRO** `sigma_ewma_delta_pct` > `19.574` → IC=-0.252 (n=309)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.574
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1421)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.155 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0028 (IC base=+0.080)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2587` → IC=+0.276 (n=65)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2587 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1066` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1066 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.333 (n=195)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.099` → IC=+0.282 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.099 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.270 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.080)

- **PATRÓN** `ibs_15` < `0.213` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.213 (IC base=-0.199)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=414)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.150 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0068 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.167 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0041 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.210 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.233 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.181 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.258 (n=324)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.175 (n=232)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.031` → IC=+0.150 (n=278)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 9.031 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=414)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.185 (n=147)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.249 (n=784)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.237 (n=784)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `0.4747` → IC=+0.255 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4747 (IC base=+0.232)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2075` → IC=+0.259 (n=355)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2075 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.232)

- **PATRÓN** `ibs_15` < `0.2756` → IC=+0.278 (n=690)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2756 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.7536` → IC=+0.311 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7536 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.912` → IC=+0.255 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.912 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.366` → IC=+0.239 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.366 (IC base=+0.232)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.253 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=507)

- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.223 (n=229)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=446)

- **FILTRO** `drift_15min` |x|> `0.8935` → IC=-0.271 (n=168)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8935
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=507)

- **FILTRO** `sigma_ewma_delta_pct` > `18.198` → IC=-0.138 (n=360)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.198
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2895)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.192 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.5625 (IC base=-0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0777` → IC=+0.228 (n=310)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0777 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.256 (n=347)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7427` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7427 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1863` → IC=+0.223 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1863 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1996` → IC=-0.207 (n=278)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1996
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=542)

- **FILTRO** `sigma_h` > `0.0197` → IC=-0.259 (n=409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=411)

- **FILTRO** `sigma_ewma_delta_pct` > `7.05` → IC=-0.207 (n=254)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.05
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=566)

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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.304 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.291 (n=722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.327 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2411` → IC=+0.307 (n=241)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2411 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.339 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8405` → IC=+0.329 (n=722)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8405 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.339 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.348 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14480.7481` → IC=+0.298 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14480.7481 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.294 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.289 (n=353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.343 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2631` → IC=+0.304 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2631 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.313 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.318 (n=394)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4139` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4139 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.367 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.328 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.310 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.312 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.297 (n=220)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3007` → IC=+0.330 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3007 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.342 (n=328)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.612` → IC=+0.308 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.612 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.329 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=217)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.134 (n=192)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=65)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.121` → IC=-0.173 (n=111)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.121
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=336)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.159 (n=42)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=129)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1681` → IC=-0.250 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1681
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

- **PATRÓN** `T_h` < `111.9965` → IC=+0.290 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9965 (IC base=+0.282)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6077 sube el IC de +0.188 a +0.267 en UPDOWN_GBM#15min (n=1802). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7061 sube el IC de +0.209 a +0.276 en UPDOWN_GBM#BTC#15min (n=399). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6559 sube el IC de +0.131 a +0.253 en UPDOWN_GBM#ETH#15min (n=379). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.174 a +0.256 en UPDOWN_GBM#SOL#15min (n=215). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.196 a +0.286 en UPDOWN_GBM#XRP#15min (n=465). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.053 a +0.150 en UPDOWN_GBM#XRP#15min (n=524). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6389 sube el IC de -0.067 a +0.270 en UPDOWN_GBM_15M_TARDIO (n=681). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3514 sube el IC de -0.028 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=2020). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.080 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=195). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.213 sube el IC de -0.199 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.147 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=324). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2756 sube el IC de +0.232 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=690). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.174 a +0.192 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=50). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.041 a +0.256 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=347). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8405 sube el IC de +0.291 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=722). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.287 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=394). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.295 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=328). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.349 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=447). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.354 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.340 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=201). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1400 | +0.099 | +197.61€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1400 | +0.099 | +197.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 29 | +0.016 | -3.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 29 | +0.016 | -3.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1056 | +0.109 | +171.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1056 | +0.109 | +171.55€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 30067 | -0.083 | -3997.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1581 | -0.027 | -213.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28486 | -0.086 | -3783.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3892 | -0.097 | -649.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3892 | -0.097 | -649.73€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1581 | -0.027 | -213.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1581 | -0.027 | -213.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3539 | -0.099 | -813.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3539 | -0.099 | -813.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7817 | -0.015 | -732.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7817 | -0.015 | -732.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7338 | -0.089 | -453.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7338 | -0.089 | -453.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5900 | -0.163 | -1134.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5900 | -0.163 | -1134.16€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 20781 | -0.025 | +3856.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5381 | +0.001 | +1790.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 15400 | -0.034 | +2065.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 20781 | -0.025 | +3856.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5381 | +0.001 | +1790.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 15400 | -0.034 | +2065.66€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1481 | -0.103 | -191.07€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 171 | -0.049 | -20.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 783 | -0.090 | -96.73€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 147 | -0.044 | -15.23€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 100909 | +0.113 | -4899.11€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14860 | +0.184 | -454.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 413 | -0.069 | -52.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 79195 | +0.101 | -4161.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6441 | +0.107 | -229.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13164 | +0.099 | -1051.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 48 | -0.160 | +1.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13101 | +0.101 | -1041.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20307 | +0.132 | -360.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4642 | +0.202 | -133.21€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13133 | +0.114 | -170.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2490 | +0.099 | -34.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13202 | +0.090 | -1171.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 54 | -0.107 | -8.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13133 | +0.092 | -1152.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21434 | +0.124 | -399.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5812 | +0.176 | -79.67€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13277 | +0.106 | -249.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2333 | +0.100 | -62.45€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19628 | +0.114 | -1137.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4255 | +0.187 | -245.20€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 316 | -0.028 | +1.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13439 | +0.092 | -761.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1618 | +0.129 | -132.84€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13174 | +0.100 | -778.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 49 | -0.029 | +9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13112 | +0.101 | -787.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16031 | +0.193 | -1015.76€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16031 | +0.193 | -1015.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3789 | +0.167 | -396.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3789 | +0.167 | -396.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1487 | +0.206 | -2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1487 | +0.206 | -2.33€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3726 | +0.181 | -310.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3726 | +0.181 | -310.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3289 | +0.241 | -101.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3289 | +0.241 | -101.46€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3661 | +0.192 | -218.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3661 | +0.192 | -218.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 755 | +0.429 | -22.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 755 | +0.429 | -22.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 294 | +0.439 | -2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 294 | +0.439 | -2.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 287 | +0.427 | -8.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 287 | +0.427 | -8.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 164 | +0.410 | -9.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 164 | +0.410 | -9.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 55414 | +0.197 | -4324.63€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 55414 | +0.197 | -4324.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9554 | +0.178 | -1083.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9554 | +0.178 | -1083.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8871 | +0.222 | -332.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8871 | +0.222 | -332.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9566 | +0.174 | -1119.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9566 | +0.174 | -1119.51€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8962 | +0.217 | -373.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8962 | +0.217 | -373.06€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9166 | +0.203 | -604.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9166 | +0.203 | -604.76€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9295 | +0.193 | -811.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9295 | +0.193 | -811.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 20981 | +0.117 | +168.53€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 20981 | +0.117 | +168.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10418 | +0.120 | +132.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10418 | +0.120 | +132.36€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10563 | +0.114 | +36.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10563 | +0.114 | +36.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1572 | +0.288 | -23.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1572 | +0.288 | -23.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 702 | +0.278 | -17.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 702 | +0.278 | -17.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 757 | +0.288 | -8.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 757 | +0.288 | -8.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 113 | +0.344 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 113 | +0.344 | +2.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 699 | +0.434 | -6.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 699 | +0.434 | -6.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 334 | +0.431 | -5.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 334 | +0.431 | -5.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 320 | +0.438 | -1.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 320 | +0.438 | -1.06€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1199 | +0.067 | -62.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 424 | +0.049 | -41.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 775 | +0.077 | -20.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 63 | +0.115 | +3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 63 | +0.115 | +3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 945 | +0.074 | -30.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 170 | +0.064 | -9.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 775 | +0.077 | -20.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 191 | +0.013 | -35.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 191 | +0.013 | -35.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 39417 | +0.098 | -1132.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3233 | +0.088 | +14.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 36184 | +0.099 | -1146.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 22020 | +0.102 | -332.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3233 | +0.088 | +14.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 18787 | +0.104 | -346.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7564 | +0.110 | -6.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7564 | +0.110 | -6.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9833 | +0.080 | -793.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9833 | +0.080 | -793.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 849 | +0.214 | -101.09€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 849 | +0.214 | -101.09€ | 2 | 4 |
| ✅ GBM_LATE_15M | 27986 | +0.085 | +13603.36€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 27986 | +0.085 | +13603.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4681 | +0.197 | +3479.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4681 | +0.197 | +3479.26€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 4162 | +0.178 | +2978.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4162 | +0.178 | +2978.51€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 4924 | +0.198 | +3669.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4924 | +0.198 | +3669.66€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4047 | +0.026 | +952.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4047 | +0.026 | +952.44€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3991 | -0.033 | +911.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3991 | -0.033 | +911.74€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 6181 | -0.040 | +1611.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6181 | -0.040 | +1611.74€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 29786 | +0.086 | +15747.40€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 29786 | +0.086 | +15747.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5673 | +0.012 | +2976.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5673 | +0.012 | +2976.52€ | 2 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6219 | +0.015 | +1329.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6219 | +0.015 | +1329.33€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4238 | +0.265 | +4307.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4238 | +0.265 | +4307.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4903 | +0.005 | +982.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4903 | +0.005 | +982.09€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4809 | +0.030 | +1891.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4809 | +0.030 | +1891.28€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3944 | +0.279 | +4261.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3944 | +0.279 | +4261.03€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 22442 | +0.170 | +17068.67€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 22442 | +0.170 | +17068.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3383 | +0.209 | +2725.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3383 | +0.209 | +2725.05€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3528 | +0.150 | +2622.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3528 | +0.150 | +2622.47€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3545 | +0.209 | +2835.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3545 | +0.209 | +2835.04€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3755 | +0.134 | +2678.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3755 | +0.134 | +2678.63€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4206 | +0.119 | +3002.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4206 | +0.119 | +3002.46€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4025 | +0.205 | +3205.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4025 | +0.205 | +3205.02€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5866 | +0.135 | +2659.15€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5866 | +0.135 | +2659.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1642 | +0.133 | +808.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1642 | +0.133 | +808.41€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1761 | +0.151 | +839.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1761 | +0.151 | +839.45€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1371 | +0.117 | +531.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1371 | +0.117 | +531.95€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 28167 | +0.177 | +21381.55€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 28167 | +0.177 | +21381.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4463 | +0.224 | +3824.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4463 | +0.224 | +3824.54€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4399 | +0.152 | +2957.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4399 | +0.152 | +2957.83€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4666 | +0.225 | +4015.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4666 | +0.225 | +4015.22€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4572 | +0.136 | +3181.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4572 | +0.136 | +3181.99€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4928 | +0.116 | +3278.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4928 | +0.116 | +3278.21€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5139 | +0.209 | +4123.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5139 | +0.209 | +4123.77€ | 0 | 26 |
| ✅ GBM_LATE_5M | 7931 | +0.164 | +5018.09€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 7931 | +0.164 | +5018.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1839 | +0.152 | +1244.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1839 | +0.152 | +1244.12€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 899 | +0.170 | +567.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 899 | +0.170 | +567.88€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 2552 | +0.166 | +1583.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2552 | +0.166 | +1583.98€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 784 | +0.145 | +411.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 784 | +0.145 | +411.05€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1938 | +0.067 | +718.21€ | 1 | 13 |
| ✅ GBM_LATE_60M#60min | 1938 | +0.067 | +718.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 713 | +0.090 | +261.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 713 | +0.090 | +261.96€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 636 | +0.069 | +283.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 636 | +0.069 | +283.45€ | 2 | 14 |
| ✅ GBM_LATE_60M#SOL | 589 | +0.035 | +172.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 589 | +0.035 | +172.81€ | 2 | 8 |
| 🚫 GBM_LATE_60M_FADE | 405 | -0.259 | -24.88€ | 10 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 405 | -0.259 | -24.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 151 | -0.226 | -8.14€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 151 | -0.226 | -8.14€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 135 | -0.259 | -8.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 135 | -0.259 | -8.36€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 119 | -0.293 | -8.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 119 | -0.293 | -8.38€ | 2 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 764 | +0.077 | +173.12€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 764 | +0.077 | +173.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 301 | +0.068 | +61.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 301 | +0.068 | +61.93€ | 3 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 228 | +0.039 | +12.27€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 228 | +0.039 | +12.27€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 235 | +0.124 | +98.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 235 | +0.124 | +98.92€ | 1 | 11 |
| ✅ LATE_WINDOW_5MIN | 107 | +0.262 | +91.86€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 107 | +0.262 | +91.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 107 | +0.262 | +91.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 107 | +0.262 | +91.86€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2215 | +0.103 | +601.50€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2215 | +0.103 | +601.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2215 | +0.103 | +601.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2215 | +0.103 | +601.50€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 396 | -0.075 | -33.15€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 396 | -0.075 | -33.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 102 | -0.048 | -3.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 102 | -0.048 | -3.77€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 145 | -0.024 | -4.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 145 | -0.024 | -4.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2182 | +0.010 | +24.30€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2182 | +0.010 | +24.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 117 | +0.021 | -2.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 117 | +0.021 | -2.45€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 252 | -0.012 | +9.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 252 | -0.012 | +9.78€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 175 | -0.025 | -5.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 175 | -0.025 | -5.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 908 | +0.023 | +22.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 908 | +0.023 | +22.12€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 494 | +0.008 | -1.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 494 | +0.008 | -1.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 236 | +0.004 | +1.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 236 | +0.004 | +1.75€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1175 | -0.040 | -23.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1175 | -0.040 | -23.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 332 | -0.042 | -13.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 332 | -0.042 | -13.16€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 398 | -0.022 | +0.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 398 | -0.022 | +0.97€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 445 | -0.055 | -11.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 445 | -0.055 | -11.06€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2527 | -0.011 | +88.64€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1207 | -0.011 | +44.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1320 | -0.011 | +44.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 74 | +0.026 | +8.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 41 | +0.058 | +8.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 33 | -0.014 | -0.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 589 | +0.011 | +46.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 275 | +0.005 | +15.85€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 314 | +0.016 | +31.05€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 321 | -0.026 | +3.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 156 | -0.057 | -7.99€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 165 | +0.003 | +11.91€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 496 | -0.026 | -9.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 229 | -0.015 | +0.08€ | 4 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 267 | -0.035 | -9.84€ | 5 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 469 | -0.001 | +31.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 234 | -0.004 | +18.84€ | 0 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 235 | +0.002 | +12.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 578 | -0.024 | +7.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 272 | -0.015 | +8.51€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 306 | -0.033 | -1.27€ | 4 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 32000 | -0.006 | +1425.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 32000 | -0.006 | +1425.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5656 | +0.019 | +702.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5656 | +0.019 | +702.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4885 | -0.030 | -66.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4885 | -0.030 | -66.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5734 | +0.015 | +504.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5734 | +0.015 | +504.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4673 | -0.053 | -155.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4673 | -0.053 | -155.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5378 | -0.009 | +211.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5378 | -0.009 | +211.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5674 | +0.009 | +229.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5674 | +0.009 | +229.25€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 6005 | -0.060 | -149.44€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6005 | -0.060 | -149.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1445 | -0.084 | -40.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1445 | -0.084 | -40.56€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 680 | -0.123 | -30.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 680 | -0.123 | -30.22€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1765 | -0.078 | -34.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1765 | -0.078 | -34.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 80779 | -0.073 | +1698.45€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 80779 | -0.073 | +1698.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13724 | -0.077 | +815.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13724 | -0.077 | +815.44€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12384 | -0.096 | -649.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12384 | -0.096 | -649.48€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 13988 | -0.067 | +728.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 13988 | -0.067 | +728.93€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11913 | -0.094 | -232.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11913 | -0.094 | -232.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14744 | -0.049 | +399.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14744 | -0.049 | +399.34€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14026 | -0.063 | +636.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14026 | -0.063 | +636.60€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7790 | -0.028 | -137.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7790 | -0.028 | -137.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1774 | -0.035 | -14.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1774 | -0.035 | -14.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2202 | -0.023 | -28.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2202 | -0.023 | -28.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1063 | -0.045 | -21.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1063 | -0.045 | -21.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 752 | -0.020 | -23.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 752 | -0.020 | -23.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1211 | +0.109 | +414.31€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1075 | +0.116 | +401.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 244 | +0.130 | +114.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 244 | +0.130 | +114.50€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 207 | +0.108 | +58.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 207 | +0.108 | +58.17€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 222 | +0.098 | +75.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 222 | +0.098 | +75.75€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 186 | +0.133 | +86.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 186 | +0.133 | +86.53€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 216 | +0.105 | +66.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 216 | +0.105 | +66.77€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 615 | -0.046 | -53.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 615 | -0.046 | -53.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 126 | -0.008 | +2.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 126 | -0.008 | +2.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 82 | -0.083 | -14.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 82 | -0.083 | -14.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 180 | -0.060 | -24.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 180 | -0.060 | -24.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 123 | -0.028 | -5.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 123 | -0.028 | -5.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 104 | -0.057 | -10.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 104 | -0.057 | -10.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 621 | -0.110 | -54.39€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 284 | -0.161 | -66.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 231 | -0.200 | -67.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 53 | +0.009 | +0.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 216 | -0.073 | -0.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 166 | -0.077 | -6.90€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 50 | -0.058 | +6.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 121 | -0.053 | +12.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 97 | -0.076 | +6.36€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 24 | +0.038 | +6.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 494 | -0.135 | -67.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 127 | -0.012 | +13.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 781 | -0.200 | -33.26€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 325 | -0.197 | -28.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 284 | -0.196 | -28.79€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 41 | -0.198 | +0.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 266 | -0.216 | -24.23€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 231 | -0.225 | -29.32€ | 4 | 0 |
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
| ✅ STREAK_FADE_15M | 551 | +0.034 | +18.42€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 551 | +0.034 | +18.42€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 266 | +0.034 | +6.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 266 | +0.034 | +6.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 57 | -0.009 | -1.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 57 | -0.009 | -1.59€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 191 | +0.034 | +10.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 191 | +0.034 | +10.66€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2864 | -0.021 | -112.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2864 | -0.021 | -112.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 845 | -0.017 | -26.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 845 | -0.017 | -26.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 572 | -0.023 | -23.22€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 572 | -0.023 | -23.22€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1291 | -0.020 | -48.70€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1291 | -0.020 | -48.70€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 76 | -0.051 | -6.76€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 76 | -0.051 | -6.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8473 | +0.022 | +121.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8473 | +0.022 | +121.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2317 | +0.024 | +30.57€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2317 | +0.024 | +30.57€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1918 | +0.031 | +48.92€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1918 | +0.031 | +48.92€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2581 | +0.011 | +3.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2581 | +0.011 | +3.39€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1657 | +0.028 | +38.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1657 | +0.028 | +38.67€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7780 | +0.013 | -39.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7780 | +0.013 | -39.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3118 | +0.016 | -9.89€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3118 | +0.016 | -9.89€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3069 | +0.013 | -17.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3069 | +0.013 | -17.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1593 | +0.008 | -11.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1593 | +0.008 | -11.86€ | 2 | 0 |
| ✅ UPDOWN_GBM | 42942 | +0.034 | +2752.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11278 | +0.071 | +2130.01€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1540 | +0.004 | +5.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 27348 | +0.025 | +597.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2612 | +0.001 | +20.30€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4374 | +0.074 | +529.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 789 | +0.160 | +340.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3552 | +0.056 | +190.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8192 | +0.041 | +598.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1450 | +0.085 | +328.86€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 412 | +0.015 | +5.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5089 | +0.041 | +234.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1179 | +0.003 | +28.57€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 62 | -0.094 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4953 | +0.041 | +313.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 746 | +0.138 | +260.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4179 | +0.024 | +54.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9374 | +0.023 | +391.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2868 | +0.049 | +329.81€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 405 | +0.006 | +6.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5163 | +0.016 | +61.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 884 | -0.003 | -10.08€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 54 | -0.125 | +3.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9809 | +0.016 | +260.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2720 | +0.027 | +191.73€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 397 | -0.004 | -1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6097 | +0.015 | +72.14€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 549 | +0.004 | +1.81€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 46 | -0.167 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6238 | +0.040 | +660.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2705 | +0.086 | +678.72€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 265 | -0.002 | -3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3268 | +0.004 | -15.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 162 | -0.128 | +0.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 595 | +0.349 | +194.83€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 595 | +0.349 | +194.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 328 | +0.354 | +105.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 328 | +0.354 | +105.26€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 267 | +0.340 | +89.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 267 | +0.340 | +89.57€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13068 | -0.036 | +2864.40€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13068 | -0.036 | +2864.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2390 | -0.122 | +32.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2390 | -0.122 | +32.94€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1475 | +0.207 | +900.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1475 | +0.207 | +900.98€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3930 | -0.064 | +583.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3930 | -0.064 | +583.68€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3915 | -0.073 | +638.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3915 | -0.073 | +638.56€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 152 | +0.039 | +8.44€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 152 | +0.039 | +8.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 152 | +0.039 | +8.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 152 | +0.039 | +8.44€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 962 | +0.291 | +773.96€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 962 | +0.291 | +773.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 525 | +0.287 | +401.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 525 | +0.287 | +401.25€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 437 | +0.295 | +372.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 437 | +0.295 | +372.71€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 736 | -0.113 | -84.24€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 736 | -0.113 | -84.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 216 | -0.083 | -16.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 216 | -0.083 | -16.24€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 71 | -0.199 | -8.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 71 | -0.199 | -8.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2597 | +0.300 | +1268.48€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 911 | +0.251 | +127.47€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 981 | +0.289 | +414.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 705 | +0.377 | +726.64€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.057) — sin ventaja clara. oversold(IBS<0.3): IC=+0.048 n=15180 | neutral: IC=+0.033 n=15975 | overbought(IBS>0.7): IC=+0.089 n=15379
  - _Datos_: n=48185 IC=+0.057 PNL=+6030.56€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 558 celda(s) pasan gate riguroso completo de 2304 evaluadas (n>=40) y 3288 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2720 IC=+0.027 PNL=+191.73€

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
  - _Estado_: 42880 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.124 n=389/60 | contraria IC=+0.169 n=364 | gap=-0.045 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=318, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 186 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=884/40 IC=-0.003 PNL=-10.08€ | BTC#60min: n=1179/40 IC=+0.003 PNL=+28.57€ | SOL#60min: n=549/40 IC=+0.004 PNL=+1.81€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=368760 | tras_1loss IC=+0.082 n=285349 | tras_2loss IC=+0.052 n=119173/40 | gap=-0.002 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.014 n=5090 | contrario_BTC IC=+0.033 n=4554/40 | gap=+0.019 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=44 PNL=+32.90€
  - _Datos_: n=44 IC=+0.239 PNL=+32.90€

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
  - _Estado_: n=55 IC=+0.184 PNL=+36.05€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=55 IC=+0.184 PNL=+36.05€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=41063 IC=+0.034 PNL=+2622.76€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=41063 IC=+0.034 PNL=+2622.76€

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
  - _Estado_: n=1812 IC=+0.005 PNL=-0.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1812 IC=+0.005 PNL=-0.91€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=800 IC=-0.009 PNL=+21.21€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=800 IC=-0.009 PNL=+21.21€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.1 con n=2402 PNL=+1542.56€
  - _Datos_: n=2402 IC=+0.188 PNL=+1542.56€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1356 IC=+0.054 PNL=+101.42€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1356 IC=+0.054 PNL=+101.42€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1450 IC=+0.085 PNL=+328.86€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1450 IC=+0.085 PNL=+328.86€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=6425 PNL=+1560.25€
  - _Datos_: n=6425 IC=+0.086 PNL=+1560.25€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=169 IC=-0.248 PNL=-5.37€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=169 IC=-0.248 PNL=-5.37€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=288 IC=-0.038 PNL=-1.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=288 IC=-0.038 PNL=-1.92€

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
  - _Estado_: n=6110 IC=-0.001 PNL=-0.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6110 IC=-0.001 PNL=-0.09€

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
  - _Estado_: n=8005 IC=+0.038 PNL=+518.14€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8005 IC=+0.038 PNL=+518.14€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2667 IC=+0.056 PNL=+326.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2667 IC=+0.056 PNL=+326.72€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=388 PNL=+121.15€
  - _Datos_: n=388 IC=+0.113 PNL=+121.15€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.149 > 0.08 con n=668 PNL=+173.45€
  - _Datos_: n=668 IC=+0.149 PNL=+173.45€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=515 PNL=+253.54€
  - _Datos_: n=515 IC=+0.113 PNL=+253.54€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=58856 IC=+0.116 PNL=+21667.79€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=58856 IC=+0.116 PNL=+21667.79€

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
  - _Estado_: n=6409 IC=+0.041 PNL=+505.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6409 IC=+0.041 PNL=+505.43€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=690 PNL=+258.25€
  - _Datos_: n=690 IC=+0.118 PNL=+258.25€

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
  - _Estado_: n=15501 IC=+0.056 PNL=+1874.94€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=15501 IC=+0.056 PNL=+1874.94€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=3911 PNL=+2153.05€
  - _Datos_: n=3911 IC=+0.203 PNL=+2153.05€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.145 < -0.1 con n=257 PNL=+30.24€
  - _Datos_: n=257 IC=-0.145 PNL=+30.24€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.1 con n=475 PNL=+136.38€
  - _Datos_: n=475 IC=+0.125 PNL=+136.38€

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
  - _Estado_: n=19964 IC=-0.137 PNL=+1407.47€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=19964 IC=-0.137 PNL=+1407.47€

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
  - _Estado_: n=2109 IC=+0.138 PNL=+1189.85€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2109 IC=+0.138 PNL=+1189.85€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.190 > 0.08 con n=2363 PNL=+1529.93€
  - _Datos_: n=2363 IC=+0.190 PNL=+1529.93€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.08 con n=530 PNL=+273.53€
  - _Datos_: n=530 IC=+0.209 PNL=+273.53€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.234 < -0.1 con n=1973 PNL=-190.78€
  - _Datos_: n=1973 IC=-0.234 PNL=-190.78€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=5869 IC=+0.174 PNL=+4009.22€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=5869 IC=+0.174 PNL=+4009.22€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=79 PNL=+29.34€
  - _Datos_: n=79 IC=+0.105 PNL=+29.34€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2149 IC=+0.067 PNL=+641.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2149 IC=+0.067 PNL=+641.37€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=1955 PNL=+1402.74€
  - _Datos_: n=1955 IC=+0.181 PNL=+1402.74€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3250 IC=-0.031 PNL=+861.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3250 IC=-0.031 PNL=+861.19€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=582 PNL=-57.85€
  - _Datos_: n=582 IC=+0.084 PNL=-57.85€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.237 > 0.08 con n=3509 PNL=-312.83€
  - _Datos_: n=3509 IC=+0.237 PNL=-312.83€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1126) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1126 IC=+0.101 PNL=+268.70€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.338 > 0.08 con n=295 PNL=+105.88€
  - _Datos_: n=295 IC=+0.338 PNL=+105.88€

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
  - _Estado_: n=9554 IC=+0.178 PNL=-1083.36€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9554 IC=+0.178 PNL=-1083.36€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.1 con n=150 PNL=+88.34€
  - _Datos_: n=150 IC=+0.197 PNL=+88.34€
